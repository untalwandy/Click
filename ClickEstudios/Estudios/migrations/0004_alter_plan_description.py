# Generated by Django 5.0 on 2024-12-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0003_alter_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]