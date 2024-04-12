from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos= models.CharField(max_length=100)
    telefono= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    linkedin= models.CharField(max_length=100)
    pub_date = models.DateTimeField("fecha update")


class Experiencia(models.Model):
    experiencia= models.ForeignKey(Persona, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=200)
    puesto = models.CharField(max_length=200)
    anios = models.IntegerField(default=0)
    inicio_date = models.DateTimeField("inicio trabajo")
    final_date = models.DateTimeField("final trabajo")