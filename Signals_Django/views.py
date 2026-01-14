

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Signals_Django! 🚀 Your server is working.")