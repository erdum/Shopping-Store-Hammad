# Generated by Django 4.2.5 on 2023-09-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_product_options_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.IntegerField(default=0),
        ),
    ]