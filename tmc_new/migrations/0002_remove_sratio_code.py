# Generated by Django 4.0.3 on 2022-04-03 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmc_new', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sratio',
            name='code',
        ),
    ]