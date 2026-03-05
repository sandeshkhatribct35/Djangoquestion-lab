from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_upload_view, name='project_upload'),
]