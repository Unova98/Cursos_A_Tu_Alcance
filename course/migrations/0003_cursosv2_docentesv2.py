# Generated by Django 3.0.3 on 2020-03-17 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_cursos_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursosV2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curso', models.CharField(max_length=100)),
                ('Hora', models.TimeField()),
                ('Fecha', models.DateField()),
                ('Ingenieria', models.CharField(max_length=40)),
                ('Aula', models.CharField(max_length=10)),
                ('Url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocentesV2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CursosV2')),
            ],
        ),
    ]
