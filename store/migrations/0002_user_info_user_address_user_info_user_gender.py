# Generated by Django 4.2.5 on 2023-09-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='user_address',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user_info',
            name='user_gender',
            field=models.CharField(default='Male', max_length=10),
        ),
    ]
