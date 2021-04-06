""" inventario models """

__author__ = 'jfoncec'

from django.db import models

class Inventario(models.Model):
    """ Model Class inventario """
    id_elemento = models.AutoField(primary_key=True)
    numero_serie = models.CharField(max_length=20)
    cantidad_elemetos = models.IntegerField()
    precio = models.FloatField()
    
    class Meta:
        db_table = 'inventario_inventario'