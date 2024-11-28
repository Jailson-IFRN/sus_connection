# Generated by Django 4.2.5 on 2023-10-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubs', '0008_alter_ubs_horario_de_inicio_and_more'),
        ('vacinas', '0002_vacinas_disponivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacinas',
            name='disponibilidade',
        ),
        migrations.AddField(
            model_name='vacinas',
            name='ubs',
            field=models.ManyToManyField(to='ubs.ubs', verbose_name='Postos em que a vacina está disponível'),
        ),
    ]
