from Vet.models import Service
from Vet.models import Appointment
from Vet.models import Doctor
from Vet.models import Schedule
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Service
        # Поля, которые мы сериализуем
        fields = ["id", "service_name", "price", "last_update", "image", "description"]


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Appointment
        # Поля, которые мы сериализуем
        fields = ["id", "phone"]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doc_name', 'doc_spec']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'doc_id', 'day', 'sch']

