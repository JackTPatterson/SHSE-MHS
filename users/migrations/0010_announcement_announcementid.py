# Generated by Django 3.2.6 on 2021-08-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_announcement_announcementid'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='announcementID',
            field=models.IntegerField(default=1233),
            preserve_default=False,
        ),
    ]
