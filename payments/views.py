from clickuz.click_authorization import click_authorization
from clickuz.serializer import ClickUzSerializer
from clickuz.status import PREPARE, COMPLETE, AUTHORIZATION_FAIL_CODE, AUTHORIZATION_FAIL
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from clickuz import ClickUz
from clickuz.views import ClickUzMerchantAPIView
from paycomuz import Paycom
from paycomuz.views import MerchantAPIView
from paycomuz.models import Transaction

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
class PaymeAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment = Payment(
                amount=data.get('amount'),
                type='Payme',
                completed=False
            )
            payment.save()
            paycom = Paycom()
            url = paycom.create_initialization(
                amount=payment.amount * 100,
                order_id=str(payment.id),
                return_url=""
            )
            return Response({
                "link": url
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckOrder(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        charge = Payment.objects.filter(id=account.get('order_id'))
        if charge.exists():
            charge = charge.first()
            if float(charge.amount) == float(amount) / 100:
                return self.ORDER_FOUND
            else:
                return self.INVALID_AMOUNT
        else:
            return self.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        transaction = Transaction.objects.filter(_id=account["id"])
        if transaction.exists():
            transaction = transaction.first()
            charge = Payment.objects.filter(id=transaction.order_key)
            if charge.exists():
                charge = charge.first()
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
            charge = Payment.objects.filter(id=transaction.order_key)
            if charge.exists():
                charge = charge.first()
                charge.delete()
                return True
            else:
                return False
        else:
            return False


class PaycomView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder