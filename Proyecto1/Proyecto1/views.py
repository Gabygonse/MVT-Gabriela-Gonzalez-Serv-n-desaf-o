from contextlib import ContextDecorator
from contextvars import Context
from pipes import Template
from django.http import HttpResponse
from django.template import Context,Template

def saludo(request):
	return HttpResponse("Hola familia")

def probandoHtml(request):
    miArchivo=open("/Users/gabygonzalez/Desktop/DESAFIO/Plantillas/template1.html")
    contenido=miArchivo.read()
    miArchivo.close()
    plantilla=Template(contenido)
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)
