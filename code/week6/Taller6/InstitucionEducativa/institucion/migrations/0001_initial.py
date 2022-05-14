# Generated by Django 4.0.4 on 2022-05-14 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('tematica', models.CharField(max_length=500)),
                ('estudiante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.estudiante')),
                ('materia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.materia')),
            ],
        ),
    ]