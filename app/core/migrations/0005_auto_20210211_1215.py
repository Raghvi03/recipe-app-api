# Generated by Django 2.1.15 on 2021-02-11 12:15

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
