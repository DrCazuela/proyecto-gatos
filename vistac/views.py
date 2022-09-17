from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def quinto(response):
    return HttpResponse("<h1>ahora mas gatitos</h1> <br> <img src='https://www.ciudaddemascotas.com/pub/media/amasty/webp/wysiwyg/4985410748_537940e266_b_jpg.webp'>")

def sexto(reponse):
    return HttpResponse("<img src='https://culturacolectiva-cultura-colectiva-prod.cdn.arcpublishing.com/resizer/XHndRgkcqf8ay2hBq0aauNQAgX0=/1024x768/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/culturacolectiva/YPFACGXXVJH3ZGSAV3G2O4ERVQ.jpg'>")

def mimanchitas(response):
    return HttpResponse('<img src="https://www.mundogato.net/wp-content/uploads/gato-carey-bebe.jpg">')

def gatopan(response):
    return HttpResponse('<img src="https://scontent.fccp2-1.fna.fbcdn.net/v/t1.18169-9/33440_162121847141427_4056621_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=101&ccb=1-7&_nc_sid=7aed08&_nc_ohc=GdNVG8cHEFQAX9PHCxy&_nc_ht=scontent.fccp2-1.fna&oh=00_AT-uut4hB9pGsd0G0rApTCEILPQA2M2CmFf_BEsgvz_71A&oe=634C99D6">')