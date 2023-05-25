from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from clickuz import ClickUz
from clickuz.views import ClickUzMerchantAPIView

from .models import *
from .serializers import *

class ClickAPIView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment = Payment(
                amount = data.get('amount'),
                type = data.get('type'),
                completed = False
            )
            payment.save()
            url = ClickUz.generate_url(
                order_id=str(payment.id),
                amount=str(payment.amount)
            )
            return Response({
                "link": url
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        charge = Payment.objects.filter(id=order_id)
        if charge.exists():
            charge = charge.first()
            if charge.amount == amount:
                return self.ORDER_FOUND
            else:
                return self.INVALID_AMOUNT
        else:
            return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        charge = Payment.objects.filter(id=order_id)
        if charge.exists():
            charge = charge.first()
            charge.completed = True
            charge.save()
            return True
        else:
            return False


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment

