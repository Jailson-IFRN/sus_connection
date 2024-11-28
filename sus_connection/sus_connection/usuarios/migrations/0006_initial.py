# Generated by Django 4.2.2 on 2023-09-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0005_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=300)),
                ('senha', models.CharField(max_length=8)),
                ('senha_confirma', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=75)),
            ],
        ),
    ]
