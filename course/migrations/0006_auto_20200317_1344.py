# Generated by Django 3.0.3 on 2020-03-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200317_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechas',
            name='Fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='horas',
            name='Hora',
            field=models.TimeField(),
        ),
    ]
