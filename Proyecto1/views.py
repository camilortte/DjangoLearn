#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
import datetime


def current_datetime(request):
	#now = datetime.datetime.now()    
	current_date = datetime.datetime.now()    
	return render_to_response( 'inicio.html' , { 'current_date' : current_date})    
	#c = Context({'current_day':now})

def saludador(request):
	nombre="Camilo"
	return render_to_response('saludos/saluda1.html',{'nombre':nombre})


def hours_ahead(request,offset):
	offset=int(offset)
	current_date_mas_tiempo  = datetime.datetime.now() + datetime.timedelta(hours=offset)	
	return render_to_response( 'hora_mas.html' , { 'mas_tiempo' : offset , 'current_date_mas_tiempo':current_date_mas_tiempo})    


