from clickuz.click_authorization import click_authorization
from clickuz.serializer import ClickUzSerializer
from clickuz.status import PREPARE, COMPLETE, AUTHORIZATION_FAIL_CODE, AUTHORIZATION_FAIL
from paycomuz.status import ORDER_FOUND, ORDER_NOT_FOND, ORDER_NOT_FOND_MESSAGE, CREATE_TRANSACTION
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from clickuz import ClickUz
from clickuz.views import ClickUzMerchantAPIView
# from paycomuz import Paycom
from paycomuz.views import MerchantAPIView
from paycomuz.models import Transaction
from datetime import datetime
from rest_framework import serializers

from .models import *
from .serializers import *


class ClickAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment = Payment(
                amount=data.get('amount'),
                type='Click',
                completed=False,
                role=data.get("role"),
                doctor_patient_id=data.get('doctor_patient_id')
            )
            payment.save()
            url = ClickUz.generate_url(
                order_id=str(payment.doctor_patient_id),
                amount=str(payment.amount)
            )
            return Response({
                "link": url
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str, param3:str, *args, **kwargs):
        charge = Payment.objects.filter(doctor_patient_id=order_id)
        if charge.exists():
            charge = charge.last()
            if charge.amount == int(amount):
                return self.ORDER_FOUND
            else:
                charge.amount = int(amount)
                if param3 == '1':
                    charge.role = 'Doktor'
                else:
                    charge.role = 'Bemor'
                charge.save()
                return self.ORDER_FOUND
        else:
            if param3 == '1':
                n = 'Doktor'
            else:
                n = 'Bemor'
            payment = Payment(
                amount=int(amount),
                type='Click',
                completed=False,
                role=n,
                doctor_patient_id=order_id
            )
            payment.save()
            return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object, *args, **kwargs):
        charge = Payment.objects.filter(doctor_patient_id=order_id)
        if charge.exists():
            charge = charge.last()
            charge.completed = True
            charge.save()
            return True
        else:
            return False


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment

    def post(self, request):
        serializer = ClickUzSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        METHODS = {
            PREPARE: self.prepare,
            COMPLETE: self.complete
        }

        merchant_trans_id = serializer.validated_data['merchant_trans_id']
        amount = serializer.validated_data['amount']
        action = serializer.validated_data['action']

        if click_authorization(**serializer.validated_data) is False:
            return Response({
                "error": AUTHORIZATION_FAIL_CODE,
                "error_note": AUTHORIZATION_FAIL
            })

        assert self.VALIDATE_CLASS != None
        check_order = self.VALIDATE_CLASS().check_order(order_id=merchant_trans_id, amount=amount, param3=request.data.get('param3'))
        if check_order is True:
            result = METHODS[action](**serializer.validated_data, response_data=serializer.validated_data)
            return Response(result)
        return Response({"error": check_order})


# Payme
from django.conf import settings
import base64
from decimal import Decimal

assert settings.PAYCOM_SETTINGS.get('KASSA_ID') != None
assert settings.PAYCOM_SETTINGS.get('ACCOUNTS') != None
assert settings.PAYCOM_SETTINGS['ACCOUNTS'].get('KEY') != None

TOKEN = settings.PAYCOM_SETTINGS['TOKEN']
KEY = settings.PAYCOM_SETTINGS['ACCOUNTS']['KEY']

class PayComResponse(object):
    LINK = 'https://checkout.paycom.uz'

    def create_initialization(self, amount: Decimal, abonent_id: str, role: str, return_url: str) -> str:
        """

        documentation : https://help.paycom.uz/ru/initsializatsiya-platezhey/otpravka-cheka-po-metodu-get

        >>> self.create_initialization(amount=Decimal(5000.00), order_id='1', return_url='https://example.com/success/')
        """

        params = f"m={TOKEN};ac.{KEY}={abonent_id};ac.role={role};a={amount};c={return_url}"
        encode_params = base64.b64encode(params.encode("utf-8"))
        encode_params = str(encode_params, 'utf-8')
        url = f"{self.LINK}/{encode_params}"
        return url

class Paycom(PayComResponse):
    ORDER_FOUND = 200
    ORDER_NOT_FOND = -31050
    INVALID_AMOUNT = -31001

    def check_order(self, amount, account, *args, **kwargs):
        """
        >>> self.check_order(amount=amount, account=account)
        """
        pass

    def successfully_payment(self, account, transaction, *args, **kwargs):
        """
        >>> self.successfully_payment(account=account, transaction=transaction)
        """
        pass

    def cancel_payment(self, account, transaction, *args, **kwargs):
        """
        >>> self.cancel_payment(account=account,transaction=transaction)
        """
        pass

class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        charge = Payment.objects.filter(doctor_patient_id=account.get('abonent_id'))
        if charge.exists():
            charge = charge.last()
            if float(charge.amount) == float(amount) / 100:
                return self.ORDER_FOUND
            else:
                charge.amount = int((amount)/100)
                charge.save()
                return self.ORDER_FOUND
        else:
            payment = Payment(
                amount=int(amount),
                type='Payme',
                completed=False,
                role=account.get("role"),
                doctor_patient_id=account.get('abonent_id')
            )
            payment.save()
            return self.ORDER_FOUND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        transaction = Transaction.objects.filter(_id=account["id"])
        if transaction.exists():
            transaction = transaction.first()
            charge = Payment.objects.filter(doctor_patient_id=transaction.order_key)
            if charge.exists():
                charge = charge.last()
                charge.completed = True
                charge.save()
                return True
            else:
                return False
        else:
            return False

    def cancel_payment(self, account, transaction, *args, **kwargs):
        transaction = Transaction.objects.filter(_id=account["id"])
        if transaction.exists():
            transaction = transaction.first()
            charge = Payment.objects.filter(doctor_patient_id=account.get('abonent_id'))
            if charge.exists():
                charge = charge.last()
                charge.delete()
                return True
            else:
                return False
        else:
            return False

class PaymeAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment = Payment(
                amount=data.get('amount'),
                type='Payme',
                completed=False,
                role=data.get("role"),
                doctor_patient_id=data.get('doctor_patient_id')
            )
            payment.save()
            paycom = Paycom()
            url = paycom.create_initialization(
                amount=payment.amount * 100,
                abonent_id=str(payment.doctor_patient_id),
                role=payment.role,
                return_url=""
            )
            return Response({
                "link": url
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaycomView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder

    user_topilmadi_xatoligi = {
    "uz": "Foydalanuvchi topilmadi.",
    "ru": "Пользователь не найден.",
    "en": "User not found."
    }

    def create_transaction(self, validated_data):
        """
        >>> self.create_transaction(validated_data)
        """
        order_key = validated_data['params']['account'].get(self.ORDER_KEY)
        if not order_key:
            raise serializers.ValidationError(f"{self.ORDER_KEY} required field")

        validate_class: Paycom = self.VALIDATE_CLASS()
        result: int = validate_class.check_order(**validated_data['params'])
        assert result != None
        if result != ORDER_FOUND:
            self.REPLY_RESPONSE[result](validated_data)
            return
        role = validated_data.get("params").get("account").get("role")
        _id = validated_data['params']['id']
        check_transaction = Transaction.objects.filter(order_key=order_key).order_by('-id')
        if check_transaction.exists():
            transaction = check_transaction.first()
            if transaction.status != Transaction.CANCELED and transaction._id == _id:
                self.reply = dict(result=dict(
                    create_time=int(transaction.created_datetime),
                    transaction=str(transaction.id),
                    state=CREATE_TRANSACTION
                ))
            elif transaction.status == Transaction.CANCELED and transaction._id != _id:
                self.reply = dict(error=dict(
                    id=validated_data['id'],
                    code=ORDER_NOT_FOND,
                    message=ORDER_NOT_FOND_MESSAGE
                ))
            else:
                current_time = datetime.now()
                current_time_to_string = int(round(current_time.timestamp()) * 1000)
                obj = Transaction.objects.create(
                    request_id=validated_data['id'],
                    _id=validated_data['params']['id'],
                    amount=validated_data['params']['amount'] / 100,
                    order_key=validated_data['params']['account'][self.ORDER_KEY],
                    state=CREATE_TRANSACTION,
                    created_datetime=current_time_to_string
                )
                self.reply = dict(result=dict(
                    create_time=current_time_to_string,
                    transaction=str(obj.id),
                    state=CREATE_TRANSACTION
                ))
        else:
            current_time = datetime.now()
            current_time_to_string = int(round(current_time.timestamp()) * 1000)
            obj = Transaction.objects.create(
                request_id=validated_data['id'],
                _id=validated_data['params']['id'],
                amount=validated_data['params']['amount'] / 100,
                order_key=validated_data['params']['account'][self.ORDER_KEY],
                state=CREATE_TRANSACTION,
                created_datetime=current_time_to_string
            )
            self.reply = dict(result=dict(
                create_time=current_time_to_string,
                transaction=str(obj.id),
                state=CREATE_TRANSACTION
            ))
        if role != "Bemor" and role != "Doktor":
            self.reply = dict(error=dict(
                code = -31050,
                message = self.user_topilmadi_xatoligi
            ))

    def check_perform_transaction(self, validated_data):
        """
        >>> self.check_perform_transaction(validated_data)
        """
        role = validated_data.get("params").get("account").get("role")
        if role != "Bemor" and role != "Doktor":
            self.reply = dict(error=dict(
                code = -31050,
                message = self.user_topilmadi_xatoligi
            ))
            return Response(self.reply)
        assert self.VALIDATE_CLASS != None
        validate_class: Paycom = self.VALIDATE_CLASS()
        result: int = validate_class.check_order(**validated_data['params'])
        assert result != None
        self.REPLY_RESPONSE[result](validated_data)


