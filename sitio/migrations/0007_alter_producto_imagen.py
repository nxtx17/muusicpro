# Generated by Django 3.2.4 on 2021-07-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(null=True, upload_to='imagenes/'),
        ),
    ]
