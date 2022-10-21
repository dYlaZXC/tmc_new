# Generated by Django 2.2.7 on 2019-12-04 05:50

from django.db import migrations


def fix_names(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.exclude(username__in=('Pavel', 'OldDbUser')):
        user.first_name, user.last_name = user.last_name, user.first_name
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_user_patronymic'),
    ]

    operations = [
        migrations.RunPython(fix_names, reverse_code=migrations.RunPython.noop)
    ]