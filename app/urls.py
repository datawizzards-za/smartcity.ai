from django.conf.urls import url
from app import views
from app import api_views
from django.contrib.auth import views as auth_views
from app import forms
urlpatterns = [

    url(r'^\Z$', views.TaskMan.as_view(), name='home'),
    url(r'^task-man/$', views.TaskMan.as_view(), name='task-man'),
    url(r'^vacancies/$', views.Vacancies.as_view(), name='vacancies'),
    url(r'^address/(?P<username>\w+)/', api_views.GetClientAddress.as_view(),
        name='address'),
    url(r'^faults/(?P<reporter>\w+)/', api_views.GetFaults.as_view(),
        name='faults'),
    url(r'^taskmanager/(?P<responder>\w+)/', api_views.GetFaults.as_view(),
        name='taskmanager'),

    url(r'^employee/', api_views.GetEmployees.as_view(), name='employee'),
    url(r'^personal/(?P<username>\w+)/', api_views.GetUser.as_view(),
        name='personal'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html',
'form_class': forms.LoginForm},
        name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', views.RegisterUserView.as_view(), name='register'),

]
