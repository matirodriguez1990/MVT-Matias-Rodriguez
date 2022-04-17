from django.http import HttpResponse
from django.shortcuts import render
from django.template import  loader
from AppFamiliar.models import Familiar

def agregar_familiares(request):
    familiar1 = Familiar(nombre="Gonzalo",apellido="Peralta",dni=1234567,fechaNac="1950-11-23",parentesco="Padre")
    familiar2 = Familiar(nombre="Susana",apellido="Perez",dni=2345678,fechaNac="1960-03-17",parentesco="Madre")
    familiar3 = Familiar(nombre="Raul",apellido="Peralta",dni=3456789,fechaNac="1980-07-04",parentesco="Hermano")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    return HttpResponse("Se agregaron familiares")

def listar_familiar(request):
    familiares = Familiar.objects.all()
    plantilla = loader.get_template("familiares.html")
    mi_contexto = {"familiares": familiares}
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)