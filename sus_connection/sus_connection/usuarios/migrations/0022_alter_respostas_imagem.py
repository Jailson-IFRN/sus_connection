# Generated by Django 4.2.2 on 2024-01-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0021_alter_duvida_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respostas',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_respostas'),
        ),
    ]
