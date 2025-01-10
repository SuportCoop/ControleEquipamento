# Generated by Django 5.0 on 2024-12-16 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_alter_controle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='products.branch', verbose_name='Filial'),
        ),
        migrations.AlterField(
            model_name='controle',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='products.category', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='controle',
            name='laptop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='products.product', verbose_name='Notebook'),
        ),
        migrations.AlterField(
            model_name='controle',
            name='phones',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='products.phone', verbose_name='Celular'),
        ),
    ]
