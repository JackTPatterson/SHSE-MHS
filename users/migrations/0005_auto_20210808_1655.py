# Generated by Django 3.2.6 on 2021-08-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210808_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='ticket',
            field=models.IntegerField(default=6574637),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='last_name',
            field=models.CharField(blank=True, max_length=254, verbose_name='Last Name'),
        ),
    ]