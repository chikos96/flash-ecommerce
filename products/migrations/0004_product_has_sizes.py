# Generated by Django 3.2 on 2021-04-28 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
