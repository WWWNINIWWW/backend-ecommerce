# Generated by Django 4.2.4 on 2023-09-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='../media/'),
            preserve_default=False,
        ),
    ]