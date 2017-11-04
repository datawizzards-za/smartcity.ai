from rest_framework import serializers
from app import models
from django.contrib.auth.models import User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ['line_one', 'line_two', 'gps', 'city', 'province']

    def create(self, validated_data):
        line_one = validated_data.get('line_one')
        line_two = validated_data.get('line_two')
        gps = validated_data.get('gps')
        city = validated_data.get('city')
        province = validated_data.get('province')
        dataset = models.Address.objects.create(line_one=line_one,
                                                line_two=line_two,
                                                gps=gps,
                                                city=city,
                                                province=province)
        return dataset


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['user', 'job_title', 'specialization', 'job_desc', 'cell']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class CitizenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = models.Citizen
        fields = ['user', 'cell']


class FaultSerializer(serializers.ModelSerializer):
    reporters = CitizenSerializer(many=True, read_only=True)
    class Meta:
        model = models.Fault
        #fields = ['uuid', 'name', 'file_url', 'created_at', 'modified_at']
        fields = ['defect', 'category', 'reporters', 'location', 
                  'date_created', 'date_submitted']

    """
    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        reporter = validated_data.get('reporter')
        location = validated_data.get('location')
        dataset = models.Address.objects.create(line_one=line_one,
                                                line_two=line_two,
                                                gps=gps,
                                                city=city,
                                                province=province)
        return dataset
    """

class CaseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CaseManager
        fields = ['fault_id', 'responder', 'status', 'reason']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def create(self, validate_data):
        username = validate_data.get('username')
        first_name = validate_data.get('first_name')
        last_name = validate_data.get('last_name')
        email = validate_data.get('email')
        password = validate_data.get('password')
        cell = validate_data.get('cell')

        user = User.objects.create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   password=password)
        dataset = models.Citizen.objects.create(user=user,
                                                cell=cell)
        return dataset
