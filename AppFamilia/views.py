from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import Familia
from django.template import Template, Context
from django.template import loader


def familia(self):

    familiar1 = Familia (nombre = "Guido", edad = "20", fechaDeNacimiento = "12/5/2001")

    familiar1.save()

    familiar2 = Familia (nombre = "Andrea", edad = "50", fechaDeNacimiento = "12/3/1972")

    familiar2.save()

    familiar3 = Familia (nombre = "Juan", edad = "29", fechaDeNacimiento = "12/5/1992")

    familiar3.save()

    listaFamiliar = [familiar1, familiar2, familiar3]

    diccionario = {"familia": listaFamiliar}

    plantilla = loader.get_template("paginaFamiliar.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)