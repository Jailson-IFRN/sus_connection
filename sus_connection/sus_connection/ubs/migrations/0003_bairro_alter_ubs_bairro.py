# Generated by Django 4.2.2 on 2023-09-23 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubs', '0002_alter_diasemana_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='ubs',
            name='bairro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubs.bairro', verbose_name='Bairro: '),
        ),
    ]
