# Generated by Django 4.2 on 2023-05-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seba',
            fields=[
                ('tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.CharField(max_length=200, verbose_name='descripcion')),
                ('precio', models.CharField(max_length=200, verbose_name='precio')),
                ('imga', models.ImageField(upload_to=None, verbose_name='')),
                ('imgb', models.ImageField(upload_to=None, verbose_name='')),
            ],
        ),
    ]
