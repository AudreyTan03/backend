# Generated by Django 4.2.10 on 2024-04-19 16:40

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=base.models.upload_image_path),
        ),
    ]
