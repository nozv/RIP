from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Vet.serializers import ServiceSerializer
from Vet.models import Service
from Vet.serializers import AppointmentSerializer
from Vet.models import Appointment
from Vet.serializers import DoctorSerializer
from Vet.models import Doctor
from Vet.serializers import ScheduleSerializer
from Vet.models import Schedule


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать услуги клиники
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer  # Сериализатор для модели


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать телефонные номера клиентов
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Appointment.objects.all().order_by('id')
    serializer_class = AppointmentSerializer  # Сериализатор для модели


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать информацию о врачах
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer  # Сериализатор для модели


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать расписание врачей
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Schedule.objects.all().order_by('id')
    serializer_class = ScheduleSerializer  # Сериализатор для модели