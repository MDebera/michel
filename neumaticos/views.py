from datetime import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Vehiculo,Empresa, Neumatico
from django.contrib.auth.models import User
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.core import serializers
import json

# -------------------------- Formulario de LOGIN DE USUARIO --------------------------------------------------
def inicio(request):
	# if request.user :
	# 	return redirect('despliegue')
	return render(request, 'neumaticos/login.html')


# -------------------------- LOGIN DE USUARIO --------------------------------------------------

def validacion(request):
	nombre = request.POST['nombre']
	passw = request.POST['password']
	user = authenticate(request, username=nombre, password=passw)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('despliegue'))

	return render(request, 'neumaticos/login.html', {'error_message': "Usuario y/o contraseña incorrecta." })

# -------------------------- Cerrar sesion --------------------------------------------------
def cerrarsesion(request):
    # logout(request)
	return redirect('inicio')


# ----------------------------- PAGINA INICIAL CON ACCIONES GENERALES ----------------------------------------------------------------------------------------------

def despliegue(request):
	empresas = Empresa.objects.all();
	neumaticos = Neumatico.objects.all();
	if request.method == 'GET' and 'e' in request.GET:
		e = int(request.GET['e'])
		vehiculos = Vehiculo.objects.filter(empresa=e);
	else:
		e = ''
		vehiculos = Vehiculo.objects.all();

	# -------------------- AGREGANDO MAILEABILIDAD QUEDA V5.5 el 13 Abril -------------------------------
	# Ponemos la accion de mail como parte dela view despliegue, cosa que se envie cada que ingresan
	# Se mailea el warning en vez de mostrarlo en de la app para ahorrar espacio visual en esta.
	# Ademas, tal warning puede recibirla alguien en el cel (aun no hay version web de la app)

	a_notificar = {} # armamos un diccio vacio que contendrá nroFuego y Profundidad de la goma a cambiar

	for i in Neumatico.objects.all(): # para cada registro en Neumatico...
		if i.Profundidad <= 5:			# si tiene 5cm o menos de Prof...
				a_notificar [i.Fuego] = str(i.Profundidad) + "CM" # pasar el NroFuego y su profundidad como key/value al dicc.
																	# Profundidad va a texto asi le apendamo "CM"
	mensaje = "Neumaticos a cambiar:" + str(a_notificar) # luego ese dix se pasa a texto...

	send_mail(
		'Notificacion neumatico2', # tema
		mensaje, # ... pues esta parte de send_mail, el mensaje ensi, debe ser una string.
		'Michelini Alerts', # remitente
		['dotaci8981@2go-mail.com'], # Recipientes. Must be a list, asi sea uno.
		fail_silently=True # TRUE: No sale error si el envio falla.
		)


	return render(request, 'neumaticos/despliegue.html',{'vehiculos': vehiculos, 'empresas':empresas, 'current_e':e, 'neumaticos':neumaticos })





#-------------------------------------- INGRESO Y/O MODIFICACION DE VEHICULOS ----------------------------------

def agregarVehiculo(request):
	empresas = Empresa.objects.all();
	return render(request, 'neumaticos/agregarVehiculo.html',{'empresas':empresas })

def modificarVehiculo(request,matricula):
	vehiculo = Vehiculo.objects.get(matricula=matricula)
	empresas = Empresa.objects.all();
	return render(request, 'neumaticos/agregarVehiculo.html',{'vehiculo':vehiculo,'empresas':empresas})

def detallesVehiculo(request,matricula):
	vehiculo = Vehiculo.objects.get(matricula=matricula)
	empresa = Empresa.objects.get(RUT=vehiculo.empresa)
	neumaticos = [
	Neumatico.objects.get(Fuego=vehiculo.posicion1),
	Neumatico.objects.get(Fuego=vehiculo.posicion2),
	Neumatico.objects.get(Fuego=vehiculo.posicion3),
	Neumatico.objects.get(Fuego=vehiculo.posicion4),
	Neumatico.objects.get(Fuego=vehiculo.posicion5),
	Neumatico.objects.get(Fuego=vehiculo.posicion6)
	]

	return render(request, 'neumaticos/detallesVehiculo.html',{'vehiculo':vehiculo,'empresa':empresa,'neumaticos':neumaticos})



#--------------# ESTA es la que realmente agrega o modifica items. Tambien es usada por la accion MODIFICABLE, abajo del todo.

def guardarVehiculo(request):
	matricula = request.POST['matricula']
	cantidad_ingresada = request.POST['cantidad']
	marca_ingresada = request.POST['marca']
	modelo_ingresado = request.POST['modelo']
	tipo_ingresado = request.POST['tipo']
	empresa_ingresada = request.POST['empresa']
	posicion1_ingresada = request.POST['posicion1']
	posicion2_ingresada = request.POST['posicion2']
	posicion3_ingresada = request.POST['posicion3']
	posicion4_ingresada = request.POST['posicion4']
	posicion5_ingresada = request.POST['posicion5']
	posicion6_ingresada = request.POST['posicion6']

	vehiculo = Vehiculo.objects.filter(matricula=matricula)
	if not vehiculo:
		vehiculo = Vehiculo(matricula=matricula)
	else:
		vehiculo = Vehiculo.objects.get(matricula=matricula)

	vehiculo.Cantidad_neumaticos = cantidad_ingresada
	vehiculo.marca = marca_ingresada
	vehiculo.modelo = modelo_ingresado
	vehiculo.Tipo_vehiculo = tipo_ingresado
	vehiculo.empresa = int(empresa_ingresada)
	vehiculo.posicion1 = posicion1_ingresada
	vehiculo.posicion2 = posicion2_ingresada
	vehiculo.posicion3 = posicion3_ingresada
	vehiculo.posicion4 = posicion4_ingresada
	vehiculo.posicion5 = posicion5_ingresada
	vehiculo.posicion6 = posicion6_ingresada
	vehiculo.save()

	return HttpResponseRedirect(reverse('despliegue'),{'message':'Vehiculo guardado con éxito'})

def eliminarVehiculo(request,matricula):
	vehiculo = Vehiculo.objects.get(matricula=matricula)
	vehiculo.delete()
	return HttpResponseRedirect(reverse('despliegue'),{'message':'Vehiculo eliminado con éxito'})

#-------------------------------------- INGRESO Y/O MODIFICACION DE Empresas ----------------------------------

def agregarEmpresa(request):
	return render(request, 'neumaticos/agregarEmpresa.html')

def modificarEmpresa(request,rut):
	empresa = Empresa.objects.get(RUT=int(rut))
	return render(request, 'neumaticos/agregarEmpresa.html',{'empresa':empresa})



def guardarEmpresa(request):
	rut = request.POST['RUT']
	nombre = request.POST['nombre']
	razon = request.POST['razon_social']
	telefono = request.POST['telefono']
	direccion = request.POST['direccion']

	empresa = Empresa.objects.filter(RUT=rut)
	if not empresa:
		empresa = Empresa(RUT=rut)
	else:
		empresa = Empresa.objects.get(RUT=rut)

	empresa.Nombre = nombre
	empresa.Razon_social = razon
	empresa.Telefono = telefono
	empresa.Direccion = direccion

	empresa.save()

	return HttpResponseRedirect(reverse('despliegue'),{'message':'Vehiculo guardado con éxito'})


def eliminarEmpresa(request,rut):
	empresa = Empresa.objects.get(RUT=rut)
	empresa.delete()
	return HttpResponseRedirect(reverse('despliegue'),{'message':'Empresa eliminada con éxito'})


#-----------------------------------------------------------------------------------------------------------
#----------------------------------INPUT DELETE MODIFY NEUMATICOS-------------------------------------------
#-----------------------------------------------------------------------------------------------------------

def agregarNeumatico(request):
	return render(request, 'neumaticos/agregarNeumatico.html')


def modificarNeumatico(request,Fuego):
	neumatico = Neumatico.objects.get(Fuego=int(Fuego))
	return render(request, 'neumaticos/modificarNeumatico.html',{'neumatico':neumatico})

def detallesNeumatico(request):
	neumatico = Neumatico.objects.get(Fuego=fuego)
	profundidad = neumatico.Profundidad
	marca = neumatico.Marca
	radio = neumatico.Radio
	talle = neumatico.Talle
	banda = neumatico.Banda
	empresa = neumatico.Empresa
	KM_Recientes = neumatico.KM_Recientes
	Cambiar_En = neumatico.Cambiar_En
	alta = neumatico.Alta
	historial = neumatico.Historial
	return render(request, 'neumaticos/detallesNeumatico.html',{'neumatico':neumatico,'profundidad':profundidad,'marca':marca, 'radio':radio, talle:'talle', 'banda':banda, 'empresa':empresa,
		'KM_Recientes': KM_Recientes, 'Cambiar_En': Cambiar_En, 'alta': alta, 'historial': historial})




def guardarNeumatico(request):
	fuego = request.POST['fuego']
	profundidad = request.POST['profundidad']
	marca = request.POST['marca']
	radio = request.POST['radio']
	talle = request.POST['talle']
	banda = request.POST['banda']
	empresa = request.POST['empresa']
	KM_Recientes = request.POST['KM_Recientes']
	Alta = request.POST['alta']

	neumatico = Neumatico.objects.filter(Fuego=fuego)
	if not neumatico:
		neumatico = Neumatico(Fuego=fuego)
	else:
		neumatico = Neumatico.objects.get(Fuego=fuego)
		mas_ahora = " \n -" + str(timezone.now().strftime('%d %m %Y')) + ": " + str(KM_Recientes) + "KMs." # y agregar usuario. Se debe mejorar con algun tipo de lista.
		neumatico.Historial = str(neumatico.Historial) + str(mas_ahora)
		neumatico.Profundidad = int(profundidad)
		neumatico.Marca = marca
		neumatico.Radio = radio
		neumatico.Talle = talle
		neumatico.Banda = banda
		neumatico.Empresa = empresa
		neumatico.KM_Recientes = int(KM_Recientes)
		neumatico.Alta = Alta
		if KM_Recientes == '0': # si ingresan 0KMs, que setée el cambiar en a CERO.
			neumatico.Cambiar_En = None
		else:
			neumatico.Cambiar_En = (int(KM_Recientes)/(15-int(profundidad)))*(int(profundidad)-3)
										#			#			#					#
										#			#			#					#
										#			#			#					#
			#KM_Recientes del ultimo control,		#			#					#
													#			#					#
											#...dividido....	#					#
																#					#
							#	#prof. usada hasta esta medicion...					#
																					#
											#...dando cuantos KMs rindio por KM usado
								#Y eso, mult por Prof. restante (osea, Profu medida menos 3)
		neumatico.save()
	return HttpResponseRedirect('modificarNeumatico/'+fuego,{'message':'Neumatico guardado con éxito'})



def eliminarNeumatico(request):
	neumatico = Neumatico.objects.get(Fuego=fuego)
	Neumatico.delete()
	return HttpResponseRedirect(reverse('despliegue'),{'message':'Neumatico eliminado con éxito'})

def filtrarNeumaticos(request,Matricula):
	vehiculo = Vehiculo.objects.get(matricula=Matricula)
	result = json.dumps({"1":vehiculo.posicion1,"2":vehiculo.posicion2,"3":vehiculo.posicion3,"4":vehiculo.posicion4,"5":vehiculo.posicion5,"6":vehiculo.posicion6})
	return HttpResponse(result)
