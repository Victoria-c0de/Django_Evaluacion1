# Generated by Django 4.2.5 on 2023-10-12 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_producto_imagen_categoria_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
    ]
