# Generated by Django 5.0 on 2024-12-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0007_caracteristica'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]