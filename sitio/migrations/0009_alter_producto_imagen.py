# Generated by Django 3.2.4 on 2021-07-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0008_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to='imagenes/productos/'),
        ),
    ]
