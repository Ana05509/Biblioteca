# Generated by Django 5.1.3 on 2024-11-12 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categorias', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id_libros', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('Fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id_ordenes', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Fecha_Ordenes', models.DateField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('id_categorias', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Biblioteca.categorias')),
                ('id_libros', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Biblioteca.libros')),
            ],
        ),
    ]
