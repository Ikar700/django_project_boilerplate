# Generated by Django 4.2.6 on 2023-11-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_price_item_normal_price_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Interesting details about the selected product'),
            preserve_default=False,
        ),
    ]