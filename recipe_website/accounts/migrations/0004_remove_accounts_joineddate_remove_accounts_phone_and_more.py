# Generated by Django 5.1 on 2024-08-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_accounts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='joinedDate',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='userEmail',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='userGender',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='userName',
        ),
    ]
