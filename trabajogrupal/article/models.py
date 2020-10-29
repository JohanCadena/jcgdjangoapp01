from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=255, verbose_name='Categoria')
    description = models.CharField(max_length=300, verbose_name='Descripcion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'

class Articulo(models.Model):
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria') 
    name = models.CharField(max_length=255, verbose_name='Nombre')
    stock = models.CharField(max_length=300, verbose_name='Piezas')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Precio')

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name= 'Articulo'
        verbose_name_plural= 'Articulos'

class Venta(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre Cliente')
    articulo_id = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name='Articulo') 
    stock = models.CharField(max_length=300, verbose_name='Piezas')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Precio')
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name= 'Venta'
        verbose_name_plural= 'Nueva Venta'