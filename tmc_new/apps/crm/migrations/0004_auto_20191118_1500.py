# Generated by Django 2.2.7 on 2019-11-18 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20191118_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcall',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.Client', verbose_name='клиент'),
        ),
    ]