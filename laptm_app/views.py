from django.shortcuts import render
from django.http import HttpResponse


def laptm_app(request):
    return HttpResponse("Hola este es el inicio de la aplicacion")
