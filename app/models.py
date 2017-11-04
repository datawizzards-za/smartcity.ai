# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=150)
    specializations = models.TextField(max_length=50)
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


class Fault(models.Model):
    defect = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField(max_length=1000, null=True)
    reporters = models.ManyToManyField(Citizen)
    #location = models.ForeignKey(Address, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    date_submitted = models.DateTimeField()
    date_created = models.DateField()
    #verification_score = models.IntegerField()


class CaseManager(models.Model):
    fault = models.ForeignKey(Fault, on_delete=models.CASCADE)
    responder = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    reason = models.CharField(max_length=150, null=True)


class Schedular(models.Model):
    fault_id = models.ForeignKey(Fault, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    recommended = models.ForeignKey(Employee, on_delete=models.CASCADE)


class TrustedReporters(models.Model):
    reporter = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    trust_score = models.IntegerField()


class ReporterRewards(models.Model):
    fault = models.ForeignKey(Fault, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Citizen, on_delete=models.CASCADE)


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    skills = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    posting_date = models.CharField(max_length=10)
    closing_date = models.CharField(max_length=10)


class Applicant(models.Model):
    user = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    qualifications = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
