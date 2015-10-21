#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms
#from django.utils.translation import ugettext_lazy as _


class HoneypotWidget(forms.TextInput):
	is_hidden = True

	def __init__(self, attrs=None, html_comment=False, *args, **kwargs):
		self.html_comment = html_comment
		super(HoneypotWidget, self).__init__(attrs, *args, **kwargs)
		if not self.attrs.has_key('class'):
			self.attrs['style'] = 'display:none'

	def render(self, *args, **kwargs):
		value = super(HoneypotWidget, self).render(*args, **kwargs)
		if self.html_comment:
			value = '<!-- %s -->' % value
		return value


class contactForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Su nombre'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Su número de teléfono'}))
	texto = forms.CharField(widget=forms.Textarea)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto
