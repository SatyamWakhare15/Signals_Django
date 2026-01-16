from django.http import HttpResponse


# home page view
def home(request):
    return HttpResponse("Welcome to Signals_Django! 🚀")