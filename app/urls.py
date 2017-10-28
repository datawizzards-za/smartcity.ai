from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^', views.EmployeeInbox.as_view(), name='employee-inbox'),
]
