# Generated by Django 2.2.7 on 2019-11-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_auto_20191129_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcall',
            name='text',
            field=models.TextField(blank=True, verbose_name='текст обращения'),
        ),
    ]