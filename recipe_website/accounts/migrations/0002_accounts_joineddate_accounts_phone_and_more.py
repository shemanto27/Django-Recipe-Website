# Generated by Django 5.1 on 2024-08-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='joinedDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='userGender',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
