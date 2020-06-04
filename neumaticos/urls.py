from django.urls import path
from . import views

urlpatterns = [
path('', views.inicio, name='inicio'),

path('validacion', views.validacion, name='validacion'),
path('cerrarsesion', views.cerrarsesion,name="cerrarsesion"),

path('despliegue', views.despliegue, name='despliegue'), #aca podemos meter matriculas para hacerles cosas o verlas

path('agregarVehiculo', views.agregarVehiculo, name='agregarVehiculo'),
path('modificarVehiculo/<matricula>', views.modificarVehiculo, name='modificarVehiculo'),
path('guardarVehiculo', views.guardarVehiculo, name='guardarVehiculo'),
path('eliminarVehiculo/<matricula>', views.eliminarVehiculo, name='eliminarVehiculo'),
path('detallesVehiculo/<matricula>', views.detallesVehiculo, name='detallesVehiculo'),

path('agregarEmpresa', views.agregarEmpresa, name='agregarEmpresa'),
path('modificarEmpresa/<rut>', views.modificarEmpresa, name='modificarEmpresa'),
path('guardarEmpresa', views.guardarEmpresa, name='guardarEmpresa'),
path('eliminarEmpresa/<rut>', views.eliminarEmpresa, name='eliminarEmpresa'),


path('agregarNeumatico', views.agregarNeumatico, name='agregarNeumatico'),
path('modificarNeumatico/<Fuego>', views.modificarNeumatico, name='modificarNeumatico'),
path('detallesNeumatico', views.detallesNeumatico, name='detallesNeumatico'),
path('guardarNeumatico', views.guardarNeumatico, name='guardarNeumatico'),
path('filtrarNeumaticos/<Matricula>', views.filtrarNeumaticos, name='filtrarNeumaticos'),

# -------------------- AGREGANDO MAILEABILIDAD QUEDA V5.5 el 13 Abril -------------------------------

# path('mandarMail', views.mandarMail, name='mandarMail'),

# ----------------------------------------------------------------------------------------------------




# path('agregargomas1', views.agregargomas1, name='agregargomas1'), #esta solamente es la page con el form empty...
# path('agregargomas2', views.agregargomas2, name='agregargomas2'), #esta solamente es la page con el form empty...
#
#
#
# path('borrar', views.borrar, name='borrar'), #esta borra. Tambien es llamada desde un form/submitdesde despliegue
# path('borrargoma', views.borrargoma, name='borrargoma'), #esta borra. Tambien es llamada desde un form/submitdesde despliegue
#
# path('modificable', views.modificable, name='modificable'), #esta borra. Tambien es llamada desde un form/submitdesde despliegue
# path('modificablegoma', views.modificablegoma, name='modificablegoma'), #esta borra. Tambien es llamada desde un form/submitdesde despliegue


]
