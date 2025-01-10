# Generated by Django 5.0 on 2024-12-16 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_controle_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='products.branch', verbose_name='Filial'),
        ),
    ]
