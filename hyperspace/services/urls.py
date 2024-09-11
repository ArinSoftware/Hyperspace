from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list')
]
