# Generated by Django 3.2.12 on 2022-06-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20220618_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='parreg',
            name='sname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]