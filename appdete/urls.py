from django.urls import path
from appdete.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clases", clases, name="clases"),
    path("profesoras", profesoras, name="profesoras"),
    path("alumnas", alumnas, name="alumnas"),
    path("clase_formulario", clase_formulario, name="clase_formulario"),
        
]
