# Generated by Django 4.0.6 on 2022-08-06 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0010_order_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='user',
        ),
    ]
