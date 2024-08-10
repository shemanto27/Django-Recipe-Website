from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registration(request):
    return render(request, "registration.html", context={'page_title' : 'Registration Page',})

def login(request):
    return render(request, "login.html", context={'page_title':'Registration Page',})