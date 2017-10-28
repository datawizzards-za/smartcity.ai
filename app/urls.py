from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'^', views.Home.as_view(), name='home'),
]
