# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from . import models
from app.forms import RegisterUserForm
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
from django.views.generic import CreateView, TemplateView
# Create your views here.


class TaskMan(View):
    template_name = 'taskman.html'

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
        description = kwargs['desc'],
        reporter = kwargs['user'],
        location = kwargs['loc'],
        )

        #context = {''}
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