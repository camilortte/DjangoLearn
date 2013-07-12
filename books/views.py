from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from books.models import Libro , Editor , Autor
from books.forms import *
from django.template import RequestContext
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

def busqueda(request):
    books = Libro.objects.all()
    eedit= Editor.objects.all()
    return render_to_response("busqueda.html",{'books': books, 'editores':eedit})

def busqueda2(request):	
	errors=[]
	if 'campo' in request.GET:	
		q = request.GET['campo']
		if not q:
			errors.append('Debe ingresar algo')
		elif len(q) > 20:
			errors.append('Por favor ingrese menos de 20 caracteres')
		else:
			books = Libro.objects.filter(title__icontains=q)			
			return render(request, 'busqueda2.html',
				{'books': books})
	return render(request, 'busqueda2.html',{'errors': errors})

def formss(request):
	if request.method == 'POST':		
		f = ContactForm2(request.POST)
		if f.is_valid():
			return HttpResponse("ES VALIDO TODO")
	else:
		f = ContactForm2()
	return render_to_response("formulario.html",{'formulario':f},context_instance=RequestContext(request))

		


