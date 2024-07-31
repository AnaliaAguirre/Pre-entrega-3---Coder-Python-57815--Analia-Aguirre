from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=40)
    comisión = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Clase: {self.nombre} - Comisión nro: {self.comisión}"
    
class Profesora(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
    
    
    
class Alumna(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"