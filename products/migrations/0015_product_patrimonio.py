# Generated by Django 5.0 on 2024-12-09 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_prestador_alter_controle_img_alter_controle_img1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='patrimonio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.prestador', verbose_name='Prestador'),
            preserve_default=False,
        ),
    ]
