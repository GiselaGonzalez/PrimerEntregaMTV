from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from.models import Cosmetologa
from.models import Manicure
from.models import Esteticista
from django.http import HttpResponse
from django.shortcuts import render
from.models import Contacto
from AppEstetic.forms import Paciente_Formulario

# Create your views here.
def Contacto(request):
    contacto=Contacto(nombre ="LadyEstetic", telefono=20996299, email="Ladyestetic@.com")
    contacto.save()
    Cadena_Texto="Contacto: "+str(Contacto.telefono)+" "+str(Contacto.email)

def esteticista(request):
    esteticista=esteticista(nombre="Adriana", apellido="Lopez")
    esteticista.save()
    cadena_Texto="Esteticista: "+Esteticista.nombre+" "+Esteticista.apellido
    return HttpResponse(cadena_Texto)

def cosmetologa(request):
    cosmetologa=Cosmetologa(nombre="Mariela", apellido="Sosa")
    cosmetologa.save()
    cadena_Texto="Cosmetologa: "+cosmetologa.nombre+" "+cosmetologa.apellido
    return HttpResponse(cadena_Texto)


def manicura(request):
    manicura=Manicure(nombre="Deborah", apellido="Maidana")
    manicura.save()
    cadena_Texto="Manicure: "+manicura.nombre+" "+manicura.apellido
    return HttpResponse(cadena_Texto)  


def inicio(request):
    return render (request,"AppEstetic/inicio.html")

def contacto(request):
    return render (request,"AppEstetic/Contacto.html")

def esteticista(request):
   return render (request,"AppEstetic/Esteticista.html")

def cosmetologa(request):
    return render(request,"AppEstetic/cosmetologa.html")


def manicura(request):
    return render (request,"AppEstetic/manicura.html")

def paciente_Formulario(request):

    if request.method==" POST":
      nombrecito=request.POST["nombre"]
      apellidito=request.POST["apellido"]

      formulario1=paciente_Formulario(nombre= nombrecito,apellido= apellidito)
      formulario1.save()
      return render(request, "AppEstetic/inicio.html")

    return render (request, "AppEstetic/paciente_Formulario.html")


def busquedaContactos(request):
    return render(request, "AppEstetic/busquedaContactos.html")


def buscar(request):
    if request.GET["nombre"]:
        busquedaContactos=request.get["nombre"]
        pacientes=busquedaContactos.objects.filter(nombre="nombre")
        return render(request, "AppEstetic/resultadoBusqueda.html")

    else:
        return render(request, "AppEstetic/busquedaContacto.html")

  


        
   




