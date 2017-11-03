# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle
import numpy as np
import json

from django.shortcuts import render
from django.views import View
from . import models
from app.forms import RegisterUserForm
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
# Create your views here.


class CaseMan(View):
    template_name = 'caseman.html'

    def get(self, request):
        #context = {''}
        return render(request, self.template_name)


class Vacancies(View):
    template_name = 'vacancies.html'

    def get(self, request):
        context = {'hello': 'hello there'}
        return render(request, self.template_name, context)


class Schedular(View):
    def get(self, request, *args, **kwargs):
        models.Faults.objects.create(
            name=kwargs['name'],
            description=kwargs['desc'],
            reporter=kwargs['user'],
            location=kwargs['loc'],
        )

        #context = {''}
        return render(request, self.template_name)


class LoadEmployeesData(View):
    template_name = 'load_employees_data.html'

    def get(self, request):
        employees_data = pickle.load(open('data/employee_data.pkl'))
        faults = json.load(open('data/faults.json'))
        string = 'EMM'
        number = 17000

        print "FAULT: ", faults[0]
        print "Length: ", len(faults)

        p = 0.1
        percent = int(len(employees_data) * p)

        assert 0
        init_numbers = ['060', '061', '062', '063', '064', '065', '071',
                        '072' '073', '074', '081', '082', '083', '084',
                        '086']

        for i in range(percent):
            emp = employees_data[i]
            names = emp['name'].split(' ')
            first_name, last_name = names[0], names[len(names) - 1]
            password = first_name + "." + last_name
            email = password + "@gmail.com"
            emp_number = string + str(number)
            number += 1

            ext_index = np.random.randint(len(init_numbers) - 1)
            phone_number = init_numbers[ext_index] + \
                str(np.random.randint(1000000, 9999999))

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=emp_number,
                email=email,
                password=password
            )

            models.Employee.objects.create(
                user=user,
                job_title=emp['title'],
                specializations=json.dumps(emp['specialisations']),
                job_desc=emp['description'],
                cell=phone_number,
            )

        for i in range(percent, len(employees_data)):
            emp = employees_data[i]
            names = emp['name'].split(' ')
            first_name, last_name = names[0], names[len(names) - 1]
            password = first_name + "." + last_name
            email = password + "@gmail.com"
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=emp_number,
                email=email,
                password=password
            )

            

        """
        class Faults(models.Model):
            defect = models.CharField(max_length=120)
            category = models.CharField(max_length=120)
            description = models.TextField(max_length=1000, null=True)
            reporter = models.ForeignKey(Citizen, on_delete=models.CASCADE)
            location = models.ForeignKey(Address, on_delete=models.CASCADE)
            data_submitted = models.DateTimeField(auto_now_add=True)
            verification_score = models.IntegerField()
        """

        return render(request, self.template_name)


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User registered')
