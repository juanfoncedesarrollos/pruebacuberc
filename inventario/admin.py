""" inventario admin"""

__author__ = 'jfoncec'

from django.contrib import admin

from inventario.models import Inventario

admin.site.register(Inventario)
