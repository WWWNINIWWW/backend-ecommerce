# Generated by Django 4.2.4 on 2023-08-30 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_concluded_order_posted_order_tracking_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedback_id',
            field=models.IntegerField(unique=True),
            preserve_default=False,
        ),
    ]
