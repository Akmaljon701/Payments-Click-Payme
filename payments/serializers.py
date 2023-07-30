from rest_framework.serializers import *

from .models import *

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount', 'type', 'completed', 'role', 'doctor_patient_id']

