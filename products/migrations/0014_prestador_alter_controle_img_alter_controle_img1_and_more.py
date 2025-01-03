# Generated by Django 5.0 on 2024-12-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_controle_img1_controle_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome')),
                ('mat', models.IntegerField(verbose_name='CNPJ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('is_inactive', models.BooleanField(verbose_name='Inativo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Prestador',
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='controle',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagem 1'),
        ),
        migrations.AlterField(
            model_name='controle',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagem 3'),
        ),
        migrations.AlterField(
            model_name='controle',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagem 3'),
        ),
    ]
