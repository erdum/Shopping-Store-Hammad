# Generated by Django 4.2.5 on 2023-09-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_user_info_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='featured',
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
