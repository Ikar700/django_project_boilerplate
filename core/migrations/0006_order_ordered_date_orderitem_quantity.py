# Generated by Django 4.2.6 on 2023-11-08 03:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default='2001-01-01', verbose_name=datetime.datetime(2023, 11, 8, 3, 28, 12, 420568, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
