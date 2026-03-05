from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointment_form_view, name='appointment_form'),
]