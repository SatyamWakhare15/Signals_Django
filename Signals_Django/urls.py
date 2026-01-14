from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),      # homepage from core app
    path('admin/', admin.site.urls),
]