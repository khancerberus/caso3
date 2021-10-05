from django.contrib import admin

from .models import Vehiculo, Cliente, Reserva

# Register your models here.
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    fields = ('patente', 'marca', 'modelo', 'anio')

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    fields = ('rut', 'nombre', 'apellidos')

@admin.register(Reserva)
class Reserva(admin.ModelAdmin):
    fields = ('id', 'motivo', 'fecha_hora')

