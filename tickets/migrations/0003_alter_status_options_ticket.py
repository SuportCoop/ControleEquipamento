# Generated by Django 5.0 on 2024-12-13 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_product_patrimonio'),
        ('tickets', '0002_status_alter_motive_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['title'], 'verbose_name': 'Status'},
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openTicket', models.DateTimeField(verbose_name='Abertura')),
                ('assumid', models.DateTimeField(verbose_name='Assumido')),
                ('responseTIcket', models.CharField(default='Caio', max_length=20)),
                ('Description', models.TextField(verbose_name='Descrição')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='filial', to='products.branch', verbose_name='Filial')),
                ('motive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='tickets.motive', verbose_name='Nome')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cooperado', to='products.cooperado', verbose_name='Nome')),
                ('serviceChannel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='controls', to='tickets.servicechannel', verbose_name='Nome')),
            ],
        ),
    ]