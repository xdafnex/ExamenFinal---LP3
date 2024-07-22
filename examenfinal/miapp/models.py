from django.db import models

# Create your models here.
class Huertas_Persona(models.Model):
    SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO)
    fecha_registro = models.DateTimeField(auto_now_add=True)