# Generated by Django 4.0.4 on 2022-05-14 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0002_paciente_fecha_de_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_de_nacimiento',
            field=models.DateField(default=datetime.datetime(2022, 5, 14, 12, 15, 51, 115448)),
        ),
    ]
