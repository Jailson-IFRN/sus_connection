# Generated by Django 5.0 on 2023-12-08 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0003_remove_vacinas_disponibilidade_vacinas_ubs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacinas',
            name='campanha',
        ),
        migrations.RemoveField(
            model_name='vacinas',
            name='data_de_vencimento',
        ),
        migrations.RemoveField(
            model_name='vacinas',
            name='lote',
        ),
    ]
