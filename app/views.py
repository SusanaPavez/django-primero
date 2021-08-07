from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hola")

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}")