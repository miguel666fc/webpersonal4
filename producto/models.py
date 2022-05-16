from django.db import models

# Create your models here.
# Crearemos la tablas para la App productos


# Creamos la tabal categoria
class Categoriaproducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProducto"
        verbose_name_plural="categoriasProducto"
    
    def __str__(self):
        return self.nombre


# Creamos la tabla producto   

class  Producto(models.Model):
    nombre_producto=models.CharField(max_length=50)
    caracteristicas=models.TextField()
    categorias=models.ForeignKey(Categoriaproducto, on_delete=models.CASCADE) # Aqui aplicamos las llave foraneas con categoria
    imagen=models.ImageField(upload_to="producto",null=True,blank=True)
    precio_neto=models.FloatField()
    precio_venta=models.FloatField()
    Estado_producto=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre_producto









