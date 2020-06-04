from django.db import models

class Vehiculo(models.Model):
	matricula = models.CharField(max_length=10,primary_key=True)
	Cantidad_neumaticos = models.IntegerField(default=0)
	marca = models.CharField(max_length=10)
	modelo = models.CharField(max_length=10)
	Tipo_vehiculo = models.CharField(max_length=10)
	empresa = models.IntegerField(max_length=50)
	posicion1 = models.IntegerField(default=0)
	posicion2 = models.IntegerField(default=0)
	posicion3 = models.IntegerField(default=0)
	posicion4 = models.IntegerField(default=0)
	posicion5 = models.IntegerField(default=0)
	posicion6 = models.IntegerField(default=0)
	def __str__(self):
		return self.matricula


class Empresa(models.Model):
	RUT = models.IntegerField(max_length=12,primary_key=True)
	Nombre = models.CharField(max_length=10)
	Razon_social = models.CharField(max_length=20)
	Direccion = models.CharField(max_length=40)
	Telefono = models.CharField(max_length=10)
	def __str__(self):
		return str(self.RUT)

class Neumatico(models.Model):
	Fuego = models.IntegerField(max_length=12,primary_key=True)
	Profundidad = models.FloatField(max_length=40)
	Marca = models.CharField(max_length=40)
	Radio = models.CharField(max_length=40)
	Talle = models.CharField(max_length=40)
	Banda = models.CharField(max_length=40)
	Empresa = models.IntegerField(max_length=12)
	#------------------------------------------------------------------------
	#KM_Recientes = models.CharField(max_length=40, default = 0)
	KM_Recientes = models.IntegerField(default=0)
	Cambiar_En = models.IntegerField(null=True, default = 0)
	Alta = models.DateField(null=True)
	Historial = models.CharField(default="Sin Cambios Aun", null=True, blank=True, max_length=1000) # deberia ser algún tipo de lista
	def __str__(self):
		return str(self.Fuego)
