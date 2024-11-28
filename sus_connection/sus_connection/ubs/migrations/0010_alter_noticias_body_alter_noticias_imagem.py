# Generated by Django 4.2.2 on 2023-10-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubs', '0009_noticias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='body',
            field=models.CharField(max_length=1000, verbose_name='Notícia'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='imagem',
            field=models.ImageField(upload_to='fotos_noticias', verbose_name='Foto ilustrativa da notícia'),
        ),
    ]
