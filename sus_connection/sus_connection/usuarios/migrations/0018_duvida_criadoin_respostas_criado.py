# Generated by Django 4.2.2 on 2024-01-07 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_remove_duvida_resposta_respostas_duvida'),
    ]

    operations = [
        migrations.AddField(
            model_name='duvida',
            name='criadoin',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respostas',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
