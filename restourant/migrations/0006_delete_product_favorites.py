# Generated by Django 4.2.4 on 2023-08-16 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restourant', '0005_alter_product_favorites_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_favorites',
        ),
    ]
