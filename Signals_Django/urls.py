from django.contrib import admin
from django.urls import path, include


# url patterns
urlpatterns = [
    path('', include('core.urls')),  # core app urls
    path('admin/', admin.site.urls),  # admin panel
]