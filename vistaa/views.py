from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def primero(response):
    return HttpResponse('<h1>Estamos iniciando</h1>')

def segundo(response):
    return HttpResponse('<h3>no desespere, estamos trabajando para usted</h3>')