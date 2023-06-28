# Generated by Django 4.1.7 on 2023-06-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='imagen'),
        ),
        migrations.AddField(
            model_name='vehiculodocumento',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='documentos/'),
        ),
    ]