# Generated by Django 3.2.6 on 2021-08-09 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_dates_dateslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='dates',
            name='dates',
            field=models.TextField(default=django.utils.timezone.now, max_length=5000, verbose_name='Message'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DatesList',
        ),
    ]
