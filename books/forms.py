from django import forms
from django.forms import ModelForm
from books.models import Autor

class ContactForm(forms.Form):
	titulo =  forms.CharField()
	email =  forms.EmailField(required=True)
	mensaje =  forms.CharField()

class ContactForm2(ModelForm):
	class Meta:
		model= Autor

