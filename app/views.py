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
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CaseMan(LoginRequiredMixin, View):
    template_name = 'caseman.html'

    def get(self, request):
        user = models.User.objects.get(username=self.request.user)
        emp = models.Employee.objects.get(user_id=user.id)
        mycases = models.CaseManager.objects.filter(responder_id=emp.id)
        new_cases = mycases.filter(status='open')
        pending = mycases.filter(status='pending')
        closed_cases = mycases.filter(status='closed')
        context = {'mycases': mycases,
                   'new_cases': new_cases, 'pending': pending,
                   'closed_cases': closed_cases}
        print(context)
        return render(request, self.template_name, context)


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
        models.Vacancy.objects.all().delete()

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
                defect=fault['defect'].title(),
                category=fault['category'].title(),
                location=fault['address'].title(),
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

            num_others = randint(0, 4)
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

        print("creating cases...")
        faults = models.Fault.objects.all()
        status = ['closed', 'open', 'pending']
        reason = ['no resources', 'high risk', 'unable to verify']
        for fault in faults:
            stat = status[np.random.randint(0, 3)]
            reas = ('', reason[np.random.randint(0, 3)])[stat == 'pending']
            try:
                employees = models.Employee.objects.filter(
                    specializations__contains=fault.category)
                employee = employees[np.random.randint(0, len(employees))]
                models.CaseManager.objects.create(
                    fault=fault,
                    responder=employee,
                    status=stat,
                    reason=reas)
            except:
                pass

        print("creating vacancies...")
        from difflib import SequenceMatcher
        import datetime
        faults = models.Fault.objects.all()
        flist = [f.category for f in faults]
        categories = list(pd.unique(flist))
        wanted_skills = []
        skills = pickle.load(open('data/skills.pkl'))
        degree = ['BSc', 'BA', 'BTech', 'Diploma', 'National Certificate']
        jds = employees.values_list('job_desc')
        jtitle = employees.values_list('job_title')

        for skill in skills:
            for cat in categories:
                if SequenceMatcher(None, cat, skill).ratio() > .4:
                    wanted_skills.append((skill, cat))

        for i in range(int(len(employees) - len(employees) * .5)):
            title = jtitle[np.random.randint(0, len(jtitle))]
            jd = jds[np.random.randint(0, len(jds))]
            cat = wanted_skills[np.random.randint(0, len(wanted_skills))][1]
            skill = pd.unique([wskills for wskills in wanted_skills if cat ==
                               wskills[1]][:np.random.randint(1, 6)])[0]
            qualifications = str(
                degree[np.random.randint(0, len(degree))]) + '., ' + title[0]
            posting = datetime.datetime.now().date() - datetime.timedelta(np.random.randint(0, 11))
            closing = posting + datetime.timedelta(np.random.randint(2, 21))

            models.Vacancy.objects.create(
                title=title[0],
                description=jd[0],
                skills=skill,
                qualifications=qualifications,
                posting_date=posting,
                closing_date=closing)

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
