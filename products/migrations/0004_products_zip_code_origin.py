# Generated by Django 4.2.4 on 2023-08-25 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_products_options_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='zip_code_origin',
            field=models.IntegerField(default=0),
        ),
    ]