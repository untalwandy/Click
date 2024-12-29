# Generated by Django 5.0 on 2024-12-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0025_estudios_img_2_alter_estudios_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='cosumidor_final',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Detalles Consumidor Final'),
        ),
        migrations.AddField(
            model_name='sale',
            name='credito_fiscal',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Detalles Fiscales'),
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_type',
            field=models.CharField(choices=[('credito', 'Crédito Fiscal'), ('consumidor', 'Consumidor Final')], default='consumidor', max_length=13, verbose_name='Tipo de Venta'),
        ),
    ]
