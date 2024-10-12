# Generated by Django 5.1.1 on 2024-10-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_trabajador', models.CharField(max_length=15)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]