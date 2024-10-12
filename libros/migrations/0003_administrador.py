# Generated by Django 5.1.1 on 2024-10-09 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_trabajador', models.CharField(max_length=10)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
        ),
    ]