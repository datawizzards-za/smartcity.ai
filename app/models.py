# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=150)
    specialization = models.CharField(max_length=50)
    job_desc = models.TextField(max_length=1000)
    cell = models.CharField(max_length=20)


class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cell = models.CharField(max_length=20)


class Address(models.Model):
    line_one = models.CharField(max_length=100)
    line_two = models.CharField(max_length=100)
    gps = models.CharField(max_length=60)
    city = models.CharField(max_length=15)
    province = models.CharField(max_length=15)


class Faults(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    reporter = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    location = models.ForeignKey(Address, on_delete=models.CASCADE)


class TaskManager(models.Model):
    fault_id = models.ForeignKey(Faults, on_delete=models.CASCADE)
    responder = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    reason = models.CharField(max_length=150)


class Recommended(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Schedular(models.Model):
    fault_id = models.ForeignKey(Faults, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    Recommended = models.ForeignKey(Recommended, on_delete=models.CASCADE)
