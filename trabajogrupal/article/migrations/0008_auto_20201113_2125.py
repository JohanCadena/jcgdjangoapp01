# Generated by Django 3.1.2 on 2020-11-14 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_carrito'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Detalle de Venta', 'verbose_name_plural': 'Detalle de Venta'},
        ),
        migrations.RemoveField(
            model_name='venta',
            name='articulo_id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='price',
        ),
    ]
