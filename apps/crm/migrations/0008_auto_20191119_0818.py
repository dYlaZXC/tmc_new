# Generated by Django 2.2.7 on 2019-11-19 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20191118_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcall',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='geo.Region', verbose_name='регион'),
        ),
    ]
