from app import serializers, models

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User


class GetClientAddress(generics.ListAPIView):
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return models.Address.objects.filter(username=username)


class GetFaults(generics.ListAPIView):
    serializer_class = serializers.FaultsSerializer

    def get_queryset(self):
        reporter = self.kwargs['reporter']
        return models.Faults.objects.filter(reporter=reporter)


class GetTaskManager(generics.ListAPIView):
    serializer_class = serializers.TaskManagerSerializer

    def get_queryset(self):
        responder = self.kwargs['responder']
        return models.TaskManager.objects.filter(responder=responder)


class GetEmployees(generics.ListAPIView):
    serializers = serializers.EmployeeSerializer

    def get_queryset(self):
        return models.Employee.objects.all()


class GetUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)