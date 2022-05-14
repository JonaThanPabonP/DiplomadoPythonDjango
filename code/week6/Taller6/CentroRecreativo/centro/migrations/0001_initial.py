# Generated by Django 4.0.4 on 2022-05-14 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('sitio_entrenamiento', models.CharField(max_length=500)),
                ('deporte_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.deporte')),
                ('deportista_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro.deportista')),
            ],
        ),
    ]