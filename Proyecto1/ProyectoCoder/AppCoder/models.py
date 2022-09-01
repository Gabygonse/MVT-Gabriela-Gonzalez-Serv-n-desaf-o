from django.db import models

# Create your models here.
class Familiar_1(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()


class Familiar_2(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()

class Familiar_3(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()