# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from . import models
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
    def get(self, requests, *args, **kwargs):
        models.Faults.objects.create(
        name=kwargs['name'],
        description = kwargs['desc'],
        reporter = kwargs['user'],
        location = kwargs['loc'],
        )

        #context = {''}
        return render(request, self.template_name)

