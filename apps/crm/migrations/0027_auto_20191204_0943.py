# Generated by Django 2.2.7 on 2019-12-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_auto_20191204_0812'),  #'0026_unset_Complaint_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='result',
            field=models.CharField(blank=True, choices=[('explanations', 'даны разъяснения'), ('justified', 'жалоба обоснована'), ('not_justified', 'жалоба не обоснована')], max_length=100, verbose_name='результат'),
        ),
    ]