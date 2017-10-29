from rest_framework import serializers
from app import models
from django.contrib.auth.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ['line_one', 'line_two', 'gps', 'city', 'province']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['user', 'job_title', 'specialization', 'job_desc', 'cell']


class FaultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faults
        fields = ['name', 'description', 'reporter', 'location']


class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskManager
        fields = ['fault_id', 'responder', 'status', 'reason']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
