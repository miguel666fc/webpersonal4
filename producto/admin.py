from django.contrib import admin
# importamos los modelos que vamos a trabajar en panel de administracion

from .models import Categoriaproducto, Producto


# Register your models here.

# se definen las  clase para los campos created y updated 
# en modo lectura
class CategoriaproductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


# se definen las  clase para los campos created y updated 
# en modo lectura
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Categoriaproducto,CategoriaproductoAdmin)

admin.site.register(Producto,ProductoAdmin)