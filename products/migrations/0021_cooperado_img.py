# Generated by Django 5.0 on 2024-12-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_controle_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperado',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagem 1'),
        ),
    ]
