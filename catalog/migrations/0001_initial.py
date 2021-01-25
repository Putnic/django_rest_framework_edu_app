# Generated by Django 2.2.3 on 2019-07-22 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('id_outer', models.CharField(max_length=100, unique=True, verbose_name='Внешний ID')),
                ('parent', models.CharField(blank=True, max_length=100, verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категории и подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('id_outer', models.CharField(max_length=100, unique=True, verbose_name='Внешний ID')),
                ('hex_code', models.CharField(max_length=100, unique=True, verbose_name='hex-код')),
            ],
            options={
                'verbose_name': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('id_outer', models.CharField(max_length=100, unique=True, verbose_name='Внешний ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, max_length=100, null=True, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Color')),
            ],
            options={
                'verbose_name': 'Товары',
            },
        ),
    ]
