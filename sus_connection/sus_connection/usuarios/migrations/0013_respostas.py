# Generated by Django 4.2.2 on 2024-01-06 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0012_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField(max_length=1000)),
                ('imagem', models.ImageField(null=True, upload_to='fotos_respostas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
