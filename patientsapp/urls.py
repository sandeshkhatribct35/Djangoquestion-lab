from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_form_view, name='patient_form'),
]