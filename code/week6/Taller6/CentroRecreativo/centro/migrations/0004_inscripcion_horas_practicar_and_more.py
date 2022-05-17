# Generated by Django 4.0.4 on 2022-05-17 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0003_alter_deportista_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='horas_practicar',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deportista',
            name='fecha_de_nacimiento',
            field=models.DateField(null=True),
        ),
    ]