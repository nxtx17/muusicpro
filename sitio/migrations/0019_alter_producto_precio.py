# Generated by Django 3.2.8 on 2022-05-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0018_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
