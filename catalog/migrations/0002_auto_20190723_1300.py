# Generated by Django 2.2.3 on 2019-07-23 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='id_outer',
            new_name='guid',
        ),
        migrations.RenameField(
            model_name='color',
            old_name='id_outer',
            new_name='guid',
        ),
        migrations.RenameField(
            model_name='color',
            old_name='hex_code',
            new_name='hexcode',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='id_outer',
            new_name='guid',
        ),
    ]
