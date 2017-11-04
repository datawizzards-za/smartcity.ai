from django.conf.urls import url
from app import views
from app import api_views
from django.contrib.auth import views as auth_views
from app import forms
urlpatterns = [
    # url(r'^createfaults/$', CreateFaults.as_view(), name='createfaults'),
    url(r'^\Z$', views.CaseMan.as_view(), name='home'),
    url(r'^case-man/$', views.CaseMan.as_view(), name='case-man'),
    url(r'^vacancies/$', views.Vacancies.as_view(), name='vacancies'),
    url(r'^visuals/$', views.Visuals.as_view(), name='visuals'),
    url(r'^rewards/$', views.Rewards.as_view(), name='rewards'),
    url(r'^notifs/$', views.Notifs.as_view(), name='notifs'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
    url(r'^load_employees_data/$', views.LoadEmployeesData.as_view(),
        name='load_employees_data'),
    url(r'^address/', api_views.GetClientAddress.as_view(),
        name='address'),
    url(r'^faults/(?P<reporter>\w+)/', api_views.GetFaultsByReporter.as_view(),
        name='faults'),
    url(r'^get_all_faults/$', api_views.GetAllFaults.as_view(),
        name='get_all_faults'),
    # url(r'^casemanager/(?P<responder>\w+)/', api_views.GetFaultsByReporter.as_view(),
    #    name='casemanager'),
    url(r'^myfaults/(?P<responder>\w+)/', api_views.GetFaultsByReporter.as_view(),
        name='myfaults'),
    url(r'^api/casemanager/', api_views.GetCaseManager.as_view(),
        name='casemanager'),
    url(r'^employee/', api_views.GetEmployees.as_view(), name='employee'),
    url(r'^personal/(?P<username>\w+)/', api_views.GetUser.as_view(),
        name='personal'),
    url(r'^api/user/', api_views.RegisterCitizen.as_view(),
        name='user'),

    url(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html', form_class=forms.LoginForm),
        name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', views.RegisterUserView.as_view(), name='register'),
]
