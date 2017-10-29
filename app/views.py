# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle

from django.shortcuts import render
from django.views import View

# Create your views here.


class TaskMan(View):
    template_name = 'taskman.html'

    def get(self, request):
        #context = {''}
        return render(request, self.template_name)


class Vacancies(View):
    template_name = 'vacancies.html'

    def get(self, request):
        #context = {''}
        return render(request, self.template_name)


class LoadEmployeesData(View):
    template_name = 'load_employees_data.html'

    """
    class Employee(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        job_title = models.CharField(max_length=150)
        specialization = models.CharField(max_length=50)
        job_desc = models.TextField(max_length=1000)
        cell = models.CharField(max_length=20)
    """

    def get(self, request):
        employees_data = pickle.load(open('data/employee_data.pkl'))
        #print employees_data
        user = request.user
        print employees_data[0]

        return render(request, self.template_name)
