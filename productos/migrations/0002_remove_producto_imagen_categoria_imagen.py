# Generated by Django 4.2.5 on 2023-10-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to='categorias'),
        ),
    ]
