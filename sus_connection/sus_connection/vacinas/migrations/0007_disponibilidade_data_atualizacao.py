# Generated by Django 4.2.2 on 2023-12-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0006_disponibilidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilidade',
            name='data_atualizacao',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
