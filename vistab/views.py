from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tercero(response):
    return HttpResponse("<img src='https://www.purina-latam.com/sites/g/files/auxxlc391/files/styles/kraken_generic_max_width_960/public/purina-10-datos-curiosos-sobre-los-gatos.png?itok=M2MiS7Mw'>")

def cuarto(response):
    return HttpResponse('<img src="https://trumboss.com/wp-content/uploads/2018/10/giong-meo-Nebelung.jpg">')