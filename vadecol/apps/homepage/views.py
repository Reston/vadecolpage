#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from vadecol.apps.homepage.forms import contactForm
from django.template import RequestContext
from django.core.mail import send_mail
from zinnia.models import Entry
from .models import Clientes
from bs4 import BeautifulSoup


def index(request):
	clientes = Clientes.objects.all()
	entradas = Entry.objects.order_by('-creation_date')
	entradas = entradas[:2]
	for ent in entradas:
		quitar_html = BeautifulSoup(ent.content, from_encoding='utf-8').get_text()
		ent.content = quitar_html[:100]
	ctx = {'entradas': entradas, 'clientes': clientes}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))


def quienessomos(request):
	return render_to_response('homepage/quienesomos.html', context_instance=RequestContext(request))


def services(request):
	return render_to_response('homepage/servicios.html', context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s' % (cd['nombre'], cd['email'])
			content = u'Email contacto: %s \nNombre o razón social: %s \nRIF o cédula: %s \nTelefono: %s \nMensaje: %s' % (cd['email'], cd['nombre'], cd['rif'], cd['telefono'], cd['texto'])
			send_mail(asunto, content, 'info@vadecol.com', ['info@vadecol.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
