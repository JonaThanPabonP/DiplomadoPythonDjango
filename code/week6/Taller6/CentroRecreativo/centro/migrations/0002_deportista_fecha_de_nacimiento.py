# Generated by Django 4.0.4 on 2022-05-14 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deportista',
            name='fecha_de_nacimiento',
            field=models.DateField(default=datetime.datetime(2022, 5, 14, 12, 7, 23, 763481)),
        ),
    ]
