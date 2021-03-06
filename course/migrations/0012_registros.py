# Generated by Django 3.0.3 on 2020-03-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20200317_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('ApellidoP', models.CharField(max_length=100)),
                ('ApellidoM', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Curso', models.CharField(max_length=100)),
                ('Docente', models.CharField(max_length=100)),
                ('Hora', models.TimeField()),
                ('Fecha', models.DateField()),
                ('Aula', models.CharField(max_length=100)),
                ('Ingenieria', models.CharField(max_length=100)),
            ],
        ),
    ]
