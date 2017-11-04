# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle
import numpy as np
import json
import datetime

from random import randint

from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from . import models
from app.forms import RegisterUserForm
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.core import serializers
# Create your views here.


class CaseMan(View):
    template_name = 'caseman.html'

    def get(self, request):
        # context = {''}
        return render(request, self.template_name)


class Vacancies(View):
    template_name = 'vacancies.html'

    def get(self, request):
        context = {'hello': 'hello there'}
        return render(request, self.template_name, context)


class Visuals(View):
    template_name = 'visuals.html'

    def get(self, request):
        context = {'hello': 'hello there'}
        return render(request, self.template_name, context)


class Notifs(View):
    template_name = 'notifs.html'

    def get(self, request):
        context = {'hello': 'hello there'}
        return render(request, self.template_name, context)


class Profile(View):
    template_name = 'profile.html'

    def get(self, request):
        context = {'hello': 'hello there'}
        return render(request, self.template_name, context)


class Rewards(View):
    template_name = 'rewards.html'

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

        # context = {''}
        return render(request, self.template_name)


class LoadEmployeesData(View):
    template_name = 'load_employees_data.html'

    def get(self, request):
        # Remove the already existing users
        print("\nBEGIN: deleting current data...")
        User.objects.all().delete()
        models.Employee.objects.all().delete()
        models.Citizen.objects.all().delete()
        models.Fault.objects.all().delete()

        print("loading employee pickel file...")
        employees_data = pickle.load(open('data/employee_data.pkl'))
        print("loading faults json file...")
        faults = json.load(open('data/faults.json'))
        len_employees = len(employees_data)
        len_faults = len(faults)
        num_employees = len_employees - len_faults

        string = 'EMM'
        number = 17000
        init_numbers = ['060', '061', '062', '063', '064', '065', '071',
                        '072' '073', '074', '081', '082', '083', '084',
                        '086']

        # Add all users
        print("\nloading employees to db...")
        print("creating auth users...")
        for emp in employees_data:
            names = emp['name'].split(' ')
            first_name, last_name = names[0], names[len(names) - 1]
            password = first_name + "." + last_name
            email = password + "@gmail.com"
            emp_number = string + str(number)
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=emp_number,
                email=email,
                password=password
            )
            number += 1

        all_users = User.objects.all()

        print("creating employees...")
        for i in range(num_employees):
            user = all_users[i]
            emp = employees_data[i]
            ext_index = np.random.randint(len(init_numbers) - 1)
            phone_number = init_numbers[ext_index] + \
                str(np.random.randint(1000000, 9999999))
            models.Employee.objects.create(
                user=user,
                job_title=emp['title'],
                specializations=json.dumps(emp['specialisations']),
                job_desc=emp['description'],
                cell=phone_number,
            )

        # Each user should atleast report one fault
        print("Creating citizens...")
        for i in range(num_employees, len(employees_data)):
            emp = employees_data[i]
            user = all_users[i]
            ext_index = np.random.randint(len(init_numbers) - 1)
            phone_number = init_numbers[ext_index] + \
                str(np.random.randint(1000000, 9999999))
            citezen1 = models.Citizen.objects.create(
                user=user,
                cell=phone_number
            )
            fault = faults[i - num_employees]
            date_created = datetime.datetime.strptime(
                fault['date_created'],
                "%Y/%m/%d"
            ).date()
            date_submitted = datetime.datetime.strptime(
                fault['date_submitted'],
                "%Y-%m-%d %H:%M:%S"
            ).date()

            m_fault = models.Fault.objects.create(
                defect=fault['defect'],
                category=fault['category'],
                location=fault['address'],
                date_created=date_created,
                date_submitted=date_submitted
            )
            m_fault.reporters.add(citezen1)
            m_fault.save()

            assert m_fault.reporters.all().count()

            print faults[i - num_employees]

        m_faults = models.Fault.objects.all()

        print("creating faults...")
        for m_fault in m_faults:
            num_others = randint(1, 4)
            other_reporters = User.objects.order_by('?')[:num_others]

            for reporter in other_reporters:
                ext_index = np.random.randint(len(init_numbers) - 1)
                phone_number = init_numbers[ext_index] + \
                    str(np.random.randint(1000000, 9999999))

                citezen = None

                try:
                    citezen = models.Citizen.objects.get(
                        user=reporter,
                    )
                except:
                    citezen = models.Citizen.objects.create(
                        user=reporter,
                        cell=phone_number
                    )

                if citezen.user != citezen1.user:
                    m_fault.reporters.add(citezen)
                    m_fault.save()

        print("DONE: complete.")

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


class LoginAuth(View):
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                username = user.username
                user = authenticate(username=username, password=password)
                login(request, user)
                details = User.objects.get(username=username)
                serialized_obj = serializers.serialize('json', [details, ])
                return HttpResponse(serialized_obj)
            else:
                return HttpResponse("{'messages':'Wrong password'}")
        except User.DoesNotExist:
            return HttpResponse("{'message':'username and password incorrect'}")
