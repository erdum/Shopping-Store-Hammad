# Generated by Django 4.2.5 on 2023-09-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_user_info_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='user_profile',
            field=models.ImageField(default='https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png', upload_to='web_images'),
        ),
    ]
