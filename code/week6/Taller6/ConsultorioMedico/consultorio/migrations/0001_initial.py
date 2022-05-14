# Generated by Django 4.0.4 on 2022-05-14 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=100)),
                ('apellido', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=100)),
                ('apellido', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cita_medica',
            fields=[
                ('uniqueId', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.TextField(max_length=500)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultorio.doctor')),
                ('paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultorio.paciente')),
            ],
        ),
    ]
