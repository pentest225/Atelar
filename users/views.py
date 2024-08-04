from django.shortcuts import render
# Create your views here.
from .models import *


def auth(request):
    print("Auth Scree")

    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')