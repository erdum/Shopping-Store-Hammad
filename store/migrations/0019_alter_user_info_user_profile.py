# Generated by Django 4.2.5 on 2023-09-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_profile',
            field=models.ImageField(default='web_images/defaultpf.jpg', upload_to='web_images'),
        ),
    ]