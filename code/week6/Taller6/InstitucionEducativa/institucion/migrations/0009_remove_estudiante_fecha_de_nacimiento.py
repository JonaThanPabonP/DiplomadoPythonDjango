# Generated by Django 4.0.4 on 2022-05-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0008_alter_estudiante_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='fecha_de_nacimiento',
        ),
    ]
