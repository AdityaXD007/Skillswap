from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')

def matching(request):
    return render(request, 'home/matching.html')

def sessions(request):
    return render(request, 'home/sessions.html')

def calendar(request):
    return render(request, 'home/calendar.html')

def base(request):
    return render(request, 'base/base.html')

def navbar(request):
    return render(request, 'base/navbar.html')

def footer(request):
    return render(request, 'base/footer.html')  
