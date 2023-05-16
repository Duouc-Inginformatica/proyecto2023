from email import message
import json #email_message
from re import I #importar libreria re
from django.http import HttpResponse #importar libreria http
from django.utils.decorators import method_decorator #importar libreria decorators
from django.http import JsonResponse #importar libreria JsonResponse
from django.shortcuts import render #importar funcion render
from django.views import View #importar clase View
from .models import Sebe #importar tabla Seba
from django.views.decorators.csrf import csrf_exempt #importar libreria csrf_exempt
import json #importar libreria json

# Create your views here.
class SebeViews(View): #crear clase SebaView

    @method_decorator(csrf_exempt) #decorar funcion
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, tipo=0): #crear funcion get
        if (tipo > 0): #si id_usuario es mayor a 0
            Datos = list(Sebe.objects.filter(tipo=tipo).values())
            if len(Datos) > 0:
                Dates = Datos[0]
                datos={'message': 'Success', 'Datos': Dates}
            else:
                datos={'message': 'No hay datos'}
        else:
            Datos=list(Sebe.objects.values()) #crear variable Datos
            if len(Datos)>0:
                datos={'message': 'Success', 'peralta': Datos} #crear variable datos
            else:
                datos={'message': 'No hay datos'}
            return JsonResponse(datos) #retornar datos


    # def post(self, request): #crear funcion post
    #     jd = json.loads(request.body) #crear variable jd
    #     Seba.objects.create(correo=jd['correo'], nombre=jd['nombre'], apellido=jd['apellido'], rut=jd['rut'],pwd=jd['pwd'])
    #     Dates={'message': 'Success'} #crear variable dates
    #     return JsonResponse (Dates) #retornar Dates

        
    # def put(self, request, rut):
    #     jd = json.loads(request.body)
    #     Datos = list(Seba.objects.filter(rut=rut).values())
    #     if len(Datos) > 0:
    #         Seba = Seba.objects.get(rut=rut)
    #         Seba.correo = jd['correo']
    #         Seba.nombre = jd['nombre']
    #         Seba.apellido = jd['apellido']
    #         Seba.rut = jd['rut']
    #         Seba.pwd = jd['pwd']
    #         Seba.save()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "Seba api not found..."}
    #     return JsonResponse(datos)

    
    
    
    
    # def delete(self, request, rut): #crear funcion delete
    #     Datos = list(Seba.objects.filter(rut=rut).values()) 
    #     if len(Datos) > 0:
    #         Seba.objects.filter(rut=rut).delete() #crear variable Datos
    #         datos={'message': 'Success'} #crear variable datos
    #     else:
    #         datos={'message': 'No hay datos'}
    #     return JsonResponse(datos) #retornar datos


