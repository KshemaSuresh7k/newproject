# Generated by Django 4.0.4 on 2022-07-04 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_rename_sid_parreg_spi_studreg_spi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parreg',
            old_name='spi',
            new_name='sid',
        ),
        migrations.RemoveField(
            model_name='studreg',
            name='spi',
        ),
    ]