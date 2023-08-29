# Generated by Django 4.2.4 on 2023-08-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_id', models.IntegerField(unique=True)),
                ('product_id', models.IntegerField(unique=True)),
                ('assessment', models.IntegerField(default=0)),
                ('comentary', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.IntegerField(unique=True)),
                ('consumer_id', models.IntegerField(unique=True)),
                ('product_id', models.IntegerField(unique=True)),
                ('zip_code_fate', models.IntegerField(default=0)),
                ('price_fate', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('price_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('quantity_buy', models.IntegerField(default=0)),
            ],
        ),
    ]