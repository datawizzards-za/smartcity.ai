from django.conf.urls import url
from app import views
from app import api_views

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

]
