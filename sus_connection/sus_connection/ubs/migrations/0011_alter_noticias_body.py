# Generated by Django 4.2.2 on 2023-10-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubs', '0010_alter_noticias_body_alter_noticias_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='body',
            field=models.TextField(max_length=1000, verbose_name='Notícia'),
        ),
    ]