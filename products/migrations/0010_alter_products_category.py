# Generated by Django 3.2.17 on 2023-02-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('Fashion', 'Fashion'), ('Beauty', 'Beauty'), ('Home & Garden', 'Home & Garden'), ('Toys & Game', 'Toys & Garden'), ('Sport & Outdoor', 'Sport & Outdoor'), ('Pet Supply', 'Pet Supply'), ('Books', 'Books'), ('Electronics', 'Electronics'), ('Car & Motorbike', 'Car & Motorbike')], default=None, max_length=50),
        ),
    ]