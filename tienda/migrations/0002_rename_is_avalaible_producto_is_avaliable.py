# Generated by Django 4.2 on 2023-05-01 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='is_avalaible',
            new_name='is_avaliable',
        ),
    ]
