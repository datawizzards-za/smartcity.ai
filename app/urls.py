from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^\Z$', views.EmployeeInbox.as_view(), name='employee-inbox'),
]
