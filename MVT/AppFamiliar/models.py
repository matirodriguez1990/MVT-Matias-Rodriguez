from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    fechaNac=models.DateField()

class Familiar(Persona):
    parentesco=models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido:{self.apellido} DNI:{self.dni} Fecha de nacimiento:{self.fechaNac} Parentesco:{self.parentesco}"