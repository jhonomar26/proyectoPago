# Generated by Django 5.0.1 on 2024-04-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correoElectronico',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
