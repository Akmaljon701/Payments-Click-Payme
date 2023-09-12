from rest_framework.serializers import *

from .models import *


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount', 'type', 'completed', 'role', 'doctor_patient_id']


class FoydalanuvchiSerializer(ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = '__all__'


class ShifokorlarSerializer(ModelSerializer):
    class Meta:
        model = Shifokorlar
        fields = '__all__'

