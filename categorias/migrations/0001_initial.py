# Generated by Django 4.2 on 2023-04-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50, unique=True)),
                ('ficha', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(max_length=250)),
                ('imag_cat', models.ImageField(blank=True, upload_to='phothos/categories')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
