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
        model = models.Fault
        fields = ['name', 'description', 'reporter', 'location']


class CaseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CaseManager
        fields = ['fault_id', 'responder', 'status', 'reason']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class FaultsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fault
        fields = ['uuid', 'name', 'file_url', 'created_at', 'modified_at']

    def create(self, validated_data):
        uuid = validated_data.get('uuid')
        name = validated_data.get('name')
        file_url = validated_data.get('file_url')

        dataset = None

        return dataset
