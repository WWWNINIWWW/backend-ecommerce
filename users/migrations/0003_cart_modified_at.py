# Generated by Django 4.2.4 on 2023-09-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]