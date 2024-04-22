from django.contrib import admin
from .models import Usuario, Ingreso, Egreso


# Añadir una lista en el panel de administracion de los campos que queremos que se muestre, estableciendo bajo que criterios se va buscar
class ingresosAdmin(admin.ModelAdmin):
    list_display = ("fechaIngreso", "categoria" )
    # Añadir una busqueda bajo los criterios que necesitamos
    search_fields = ("fechaIngreso", "categoria")
# Añadir una lista en el panel de administracion de los campos que queremos que se muestre, estableciendo bajo que criterios se va buscar
class egresosAdmin(admin.ModelAdmin):
    list_display = ("fechaIngreso", "categoria" )
    # Añadir una busqueda bajo los criterios que necesitamos
    search_fields = ("fechaIngreso", "categoria")


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ingreso, ingresosAdmin)
# admin.site.register(Ingreso)
admin.site.register(Egreso,egresosAdmin)
