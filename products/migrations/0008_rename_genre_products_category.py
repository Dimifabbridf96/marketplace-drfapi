# Generated by Django 3.2.17 on 2023-02-03 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20230203_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='genre',
            new_name='category',
        ),
    ]
