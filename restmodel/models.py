from django.db import models

# Create your models here.
class RestModel (models.Model):
    nombre=models.CharField(max_length=100,blank=True,null=True)
    apellido=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.nombre