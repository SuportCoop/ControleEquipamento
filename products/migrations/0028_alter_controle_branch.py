# Generated by Django 5.0 on 2024-12-16 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_product_patrimonio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='branch',
            field=models.ForeignKey(default='sede', on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='products.branch', verbose_name='Filial'),
        ),
    ]
