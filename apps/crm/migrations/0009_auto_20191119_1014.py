# Generated by Django 2.2.7 on 2019-11-19 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20191119_0818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientcall',
            options={'ordering': ['-created'], 'verbose_name': 'обращение в КЦ', 'verbose_name_plural': 'обращения в КЦ'},
        ),
    ]
