from django.shortcuts import render
from django.views.generic import TemplateView
import random

def home(request):
    return render(request, 'home.html')

def generate_password(request):
    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        char.extend(list('0123456789'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*'))
    
    length = int(request.GET.get('length', 7))
    password = ''
    for _ in range(length):
        password += random.choice(char)

    return render(request, 'password.html', {'password' : password, 'print' : length})

def about(request):
    return render(request, 'about.html')