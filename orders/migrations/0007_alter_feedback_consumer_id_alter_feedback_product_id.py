# Generated by Django 4.2.4 on 2023-09-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_feedback_feedback_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='consumer_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='product_id',
            field=models.IntegerField(),
        ),
    ]