from importlib.resources import contents
from multiprocessing import context
import re  #importar libreria re
from tkinter import EW #importar libreria tkinter
from django.shortcuts import render, redirect 
from api.models import Sebe #importar la tabla seba
from api.forms import SebeForm #importar formulario
from django.conf import settings

# Create your views here.
# Create your views here.

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