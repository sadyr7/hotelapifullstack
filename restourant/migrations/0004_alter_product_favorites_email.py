# Generated by Django 4.2.4 on 2023-08-16 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restourant', '0003_rename_user_product_favorites_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_favorites',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
