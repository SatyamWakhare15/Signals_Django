from django.urls import path
from . import views


# core app url patterns
urlpatterns = [
    path('', views.home, name='home'),
]