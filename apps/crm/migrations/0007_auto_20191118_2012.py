# Generated by Django 2.2.7 on 2019-11-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_create_basic_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcall',
            name='topics',
            field=models.ManyToManyField(blank=True, to='crm.Topic', verbose_name='темы'),
        ),
    ]