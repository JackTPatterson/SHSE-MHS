# Generated by Django 3.2.6 on 2021-08-09 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_dates_datesid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='datesID',
        ),
    ]
