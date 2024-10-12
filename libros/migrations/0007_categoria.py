# Generated by Django 5.1.1 on 2024-10-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_docente_qr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
