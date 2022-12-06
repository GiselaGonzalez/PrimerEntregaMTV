from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre +" "+str(self.telefono)+" "+ str(self.email)


class Esteticista(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)

    def __str__(self):
        return self. nombre +" "+self. apellido

class Cosmetologa(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Manicure(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Paciente_Formulario(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido




