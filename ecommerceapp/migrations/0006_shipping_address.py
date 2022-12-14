# Generated by Django 4.0.6 on 2022-08-05 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerceapp', '0005_zip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=12)),
                ('House', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=60)),
                ('Landmark', models.CharField(max_length=60)),
                ('Town', models.CharField(max_length=60)),
                ('State', models.CharField(max_length=60)),
                ('Zip', models.IntegerField()),
                ('Order_note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
