# Generated by Django 3.2.12 on 2022-05-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_eventadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date', models.DateField()),
                ('days', models.IntegerField()),
                ('reason', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
