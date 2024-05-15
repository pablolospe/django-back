from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import *
from django.shortcuts import redirect

def index(request):
    context={
        'nombre': 'Ernesto',
        'fecha': datetime.datetime.now()
    }

    return render(request, 'web/index.html', context)

def saludar(request, nombre):
    return HttpResponse('hola {nombre}')

def lista(request):
    context={
        'alumnos': [
            {'name':'pepe monje', 'cuota_al_dia':True},
            {'name':'luis luque', 'cuota_al_dia':False},
            {'name':'marta sanchez', 'cuota_al_dia':False},
            {'name':'luz arribas', 'cuota_al_dia':True},
        ]
    }
    return render(request, 'web/lista.html', context)

# def form(request):
#     context = {}

#     if request.method == "GET":
#         context['form'] = UsuarioForm()

#     else: 
#         context['form'] = UsuarioForm(request.POST)
#         print('hey')
#         return redirect('index')


#     return render(request, 'web/form.html', context)


def form(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['form'] = UsuarioForm()
    
    else: # Asumo que es un POST
        contexto['form'] = UsuarioForm(request.POST)
        
        # Validar el form

        # Si el form es correcto
        # Lo redirijo a una vista segura por ejemplo el index

        # Si el form es incorrecto
        # renderizo un form con mensajes de error
        
        print(request.POST)

        return redirect('index')

    return render(request, 'web/form.html', contexto)