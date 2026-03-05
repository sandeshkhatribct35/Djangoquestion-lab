from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('labapp.urls')),
    path('patients/', include('patientsapp.urls')),
    path('users/', include('usersapp.urls')),
    path('upload/', include('uploadapp.urls')),
    path('project/', include('projectapp.urls')),
    path('appointment/', include('advancedformapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)