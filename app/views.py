from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola")

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}")