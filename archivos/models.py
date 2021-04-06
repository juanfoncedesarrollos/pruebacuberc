""" archivos models """

__author__ = 'jfoncec'

import datetime
from django.db import models

class Archivos(models.Model):

    id_archivo = models.AutoField(primary_key=True)
    nombre_archivo = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_created=True)
    archivo = models.FileField(upload_to="archivos/data/", null=True, blank=True)

    class Meta:
    
        db_table = 'archivos_archivos'

    def __str__(self):
        return self.nombre_archivo

    def creado_resiente(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)


