# Generated by Django 5.0 on 2023-12-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubs', '0013_noticias_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='data',
            field=models.DateTimeField(null=True, verbose_name='Data da notícia ou do Informe: '),
        ),
    ]