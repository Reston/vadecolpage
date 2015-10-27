# coding: utf-8
from django.db import models


class Clientes(models.Model):
	imagen = models.ImageField(upload_to='imgClientes')
	alt = models.CharField(max_length=100)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)
