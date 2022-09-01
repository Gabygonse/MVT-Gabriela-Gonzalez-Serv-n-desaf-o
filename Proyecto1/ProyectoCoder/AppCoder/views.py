from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.


def Familiar_1(self):
    familiar_1= Familiar_1(nombre="Pamela",edad="20",fecha_nacimiento="2001-11-23")
    familiar_1.save()
    documentoDeTexto=f"nombre:{Familiar_1.nombre} edad:{Familiar_1.edad} fecha_nacimiento:{Familiar_1.fecha_nacimiento} "
    return HTTPResponse(documentoDeTexto)

def Familiar_2(self):
    familiar_2= Familiar_2(nombre="Miguel",edad="62",fecha_nacimiento="1960-07-09")
    familiar_2.save()
    documentoDeTexto=f"nombre:{Familiar_2.nombre} edad:{Familiar_2.edad} fecha_nacimiento:{Familiar_2.fecha_nacimiento} "
    return HTTPResponse(documentoDeTexto)

def Familiar_3(self):
    familiar_3= Familiar_3(nombre="Gaby",edad="52",fecha_nacimiento="1970-09-14")
    familiar_3.save()
    documentoDeTexto=f"nombre:{Familiar_3.nombre} edad:{Familiar_3.edad} fecha_nacimiento:{Familiar_3.fecha_nacimiento} "
    return HTTPResponse(documentoDeTexto)