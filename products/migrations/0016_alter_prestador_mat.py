# Generated by Django 5.0 on 2024-12-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_patrimonio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestador',
            name='mat',
            field=models.CharField(max_length=20, verbose_name='CNPJ'),
        ),
    ]
