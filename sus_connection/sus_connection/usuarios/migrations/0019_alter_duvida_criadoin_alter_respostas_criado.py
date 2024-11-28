# Generated by Django 4.2.2 on 2024-01-07 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_duvida_criadoin_respostas_criado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duvida',
            name='criadoin',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='respostas',
            name='criado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]