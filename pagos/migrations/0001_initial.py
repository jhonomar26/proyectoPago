# Generated by Django 5.0.1 on 2024-04-18 02:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nomUsuario', models.CharField(max_length=100, null=True)),
                ('totalIngresos', models.PositiveIntegerField(null=True)),
                ('totalEgreso', models.PositiveIntegerField(null=True)),
                ('totalGanancias', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField(null=True)),
                ('monto', models.FloatField(null=True)),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=255, null=True)),
                ('Usuario_idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField(null=True)),
                ('monto', models.FloatField(null=True)),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=255, null=True)),
                ('Usuario_idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.usuario')),
            ],
        ),
    ]
