from contextvars import Context
import logging
from multiprocessing import context
from pipes import Template
from urllib import request
from xml.dom.minidom import Document
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def login(request): #primera vista
    doc_externo = open("G:/pyhton/django/proyectos2/Tienda/Tienda/plantillas/login.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def Productos(request): #primera vista
    doc_externo = open("G:/pyhton/django/proyectos2/Tienda/Tienda/plantillas/productos.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)