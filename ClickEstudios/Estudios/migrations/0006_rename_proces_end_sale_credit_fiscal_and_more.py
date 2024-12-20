# Generated by Django 5.0 on 2024-12-18 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0005_client_plan_time_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='proces_end',
            new_name='credit_fiscal',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='description_plane',
            new_name='description_plan',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='mont_reserv',
            new_name='mount',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='sale_payment',
            new_name='payment',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='start_date',
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='date_choice',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha final'),
        ),
        migrations.AddField(
            model_name='sale',
            name='end_proces_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha final'),
        ),
        migrations.AddField(
            model_name='sale',
            name='finalize',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sale',
            name='start_proces_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_adicionales', to='Estudios.sale')),
            ],
            options={
                'verbose_name': 'adicional',
                'verbose_name_plural': 'adicionales',
            },
        ),
    ]
