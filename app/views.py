# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View


# Create your views here.


class EmployeeInbox(View):
    template_name = 'employee.inbox.html'

    def get(self, request):
        #context = {''}
        return render(request, self.template_name)
