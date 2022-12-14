# Generated by Django 2.2.7 on 2019-11-26 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20191126_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcall',
            name='operator',
        ),
        migrations.AlterField(
            model_name='clientcall',
            name='kind',
            field=models.CharField(choices=[('consultation', 'консультация'), ('complaint', 'жалоба'), ('thanks', 'благодарность'), ('wrong_call', 'ошибочный звонок')], default='consultation', max_length=100, verbose_name='вид'),
        ),
        migrations.AlterField(
            model_name='clientcall',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='organizations.Organization', verbose_name='МО'),
        ),
    ]
