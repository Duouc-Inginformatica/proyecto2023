from importlib.resources import contents
from multiprocessing import context
import re  #importar libreria re
from tkinter import EW #importar libreria tkinter
from django.shortcuts import render, redirect 
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from api.models import Sebe #importar la tabla seba
from api.forms import SebeForm #importar formulario
from django.conf import settings
from .models import *

# Create your views here.
# Create your views here.

import requests

import requests
import json

def enindex(request):
    response = requests.get('https://v6.exchangerate-api.com/v6/72552993d706facefc816853/pair/USD/CLP')
    dato = response.json()
    # dolar = dato.get('conversion_rate')
    # data = float(Peralta) // float(dolar)
    # float1 = Peralta
    # int1 = int(float1)
    geto = dato.get('conversion_rate')
    variable = int(geto)
    Sebas = Sebe.objects.all()
    dolar = dato.get('time_last_update_utc')

    next = dato.get('time_next_update_utc')
    # data = Peralta / int2
    # process the data as needed
    prices1 = [seba.precio for seba in Sebas]
    total = round(sum([s.precio for s in Sebas]) / variable, 2)
    context = {'Sebas': Sebas, 'total':total, 'prices1': prices1, 'dolar': dolar, 'next':next}
    return render(request, 'enindex.html', context)

# def enindex(request):
#     url = requests.get('')
#     response = requests.get(url)
#     if response.status_code == 200:
#         # api_data = json.loads(response.content)
#         data = response.json()
#         # Aquí puedes acceder a los datos específicos que necesites
#         # datos = api_data['conversion_rate']
#         return render(request, 'enindex.html', {'data': data})
#     else:
#         # Si no se puede conectar a la API
#         return render(request, 'error.html')


def index(request): #crear funcion index
    Sebas = Sebe.objects.all() #crear variable maules y llamar a la tabla maule
    return render(request, 'index.html', {'Sebas': Sebas}) #enviar datos a la pagina index.html en variable maules


def homies(request):
    return render(request, 'homies.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def imgs(request):
    return render(request, document_root=settings.MEDIA_ROOT)