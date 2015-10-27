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
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Su nombre o empresa'}))
	rif = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'J-99999999-9 | 9999999'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Su número de teléfono'}))
	texto = forms.CharField(widget=forms.Textarea)
	website = forms.CharField(widget=HoneypotWidget, required=False)

	def clean_website(self):
		cd = self.cleaned_data
		website = cd.get('website')
		if len(website)>0:
			raise forms.ValidationError('Anti-spam field changed in value.')
		if website != '':
			raise forms.ValidationError('Anti-spam field changed in value.')

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
