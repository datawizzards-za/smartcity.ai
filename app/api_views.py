from app import serializers, models

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from app import models
from app import serializers


class GetFaultsByReporter(generics.ListAPIView):
    serializer_class = serializers.FaultsSerializer

    def get_queryset(self):
        reporter = self.kwargs['reporter']
        user = User.objects.get(username=reporter)
        return models.Fault.objects.filter(reporters=user.username)


class GetAllFaults(generics.ListCreateAPIView):
    queryset = models.Fault.objects.all()
    serializer_class = serializers.FaultSerializer


class RegisterCitizen(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class ListCreateCitizen(generics.ListCreateAPIView):
    queryset = models.Citizen.objects.all()
    serializer_class = serializers.CitizenSerializer


class GetCaseManager(generics.ListAPIView):
    serializer_class = serializers.CaseManagerSerializer

    def get_queryset(self):
        responder = self.kwargs['responder']
        return models.CaseManager.objects.filter(responder=responder)


class GetEmployees(generics.ListAPIView):
    serializers = serializers.EmployeeSerializer

    def get_queryset(self):
        return models.Employee.objects.all()


class GetUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)


class GetClientAddress(generics.ListCreateAPIView):
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        return models.Address.objects.all()
