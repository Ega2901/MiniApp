from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Главная</h1>')


def tasks(request):
    return HttpResponse('<h1>Наш клуб</h1>')


from django.shortcuts import render

# Create your views here.
