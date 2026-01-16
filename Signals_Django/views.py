from django.http import HttpResponse


# basic home view
def home(request):
    return HttpResponse("Welcome to Signals_Django! 🚀 Your server is working.")