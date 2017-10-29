from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^\Z$', views.TaskMan.as_view(), name='home'),
    url(r'^task-man/$', views.TaskMan.as_view(), name='task-man'),
    url(r'^vacancies/$', views.Vacancies.as_view(), name='vacancies'),
]
