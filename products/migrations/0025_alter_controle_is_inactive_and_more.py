# Generated by Django 5.0 on 2024-12-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_phone_number_alter_controle_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='is_inactive',
            field=models.BooleanField(default=False, verbose_name='Inativo'),
        ),
        migrations.AlterField(
            model_name='cooperado',
            name='is_inactive',
            field=models.BooleanField(default=False, verbose_name='Inativo'),
        ),
    ]
