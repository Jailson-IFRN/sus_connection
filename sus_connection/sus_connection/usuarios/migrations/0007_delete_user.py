# Generated by Django 4.2.2 on 2023-09-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]