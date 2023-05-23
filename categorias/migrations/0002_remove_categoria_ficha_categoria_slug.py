# Generated by Django 4.2 on 2023-04-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='ficha',
        ),
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
