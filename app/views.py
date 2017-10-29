# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
