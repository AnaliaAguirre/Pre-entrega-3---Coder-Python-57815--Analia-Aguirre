from django.shortcuts import render
from django.http import HttpResponse
from appdete import views

# Create your views here.
def inicio(request):
    return render(request, "appdete/padre.html")
def clases(request):
    return render(request, "appdete/padre.html")
def profesoras(request):
    return render(request, "appdete/padre.html")
def alumnas(request):
    return render(request, "appdete/padre.html")

from appdete.models import Clase
def clase_formulario(request):
    if request.method == 'POST':
        clase = Clase(nombre=request.POST['clase'], comisión=request.POST['comisión'])
        clase.save()
        return render(request, "appdete/padre.html")
    return render(request, "appdete/clase_formulario.html")
