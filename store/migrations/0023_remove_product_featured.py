# Generated by Django 4.2.5 on 2023-09-09 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
    ]