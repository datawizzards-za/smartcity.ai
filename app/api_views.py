from app import serializers, models

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User


class GetClientAddress(generics.ListCreateAPIView):
    serializer_class = serializers.AddressSerializer

    def get(self, *args, **kwargs):
        """Retrieve result base on the clustering result id

        Kwargs:
            kwargs['pk'] (str): Clustering algorithm id.

        """

        pk = kwargs['pk']
        algo_name = kwargs['algo']
        queryset = None
        serializer = None

        queryset = self.get_queryset(pk, algo_name)
        serializer = serializers.FaultsCreateSerializer(queryset, many=False)

        return Response(serializer.data)

    def get_queryset(self,  fault_id):
        queryset = models.Faults.filter(name=fault_id)
        return queryset


class GetFaults(generics.ListAPIView):
    serializer_class = serializers.FaultsSerializer

    def get_queryset(self):
        reporter = self.kwargs['reporter']
        return models.Faults.objects.filter(reporter=reporter)


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
