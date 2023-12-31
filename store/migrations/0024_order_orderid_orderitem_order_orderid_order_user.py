# Generated by Django 4.2.5 on 2023-09-10 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0023_remove_product_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=200)),
                ('phone', models.TextField(max_length=15)),
                ('sub_total', models.IntegerField()),
                ('shipping_charges', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discount', models.IntegerField(default=0)),
                ('image', models.ImageField(default='web_images/store/imagenotfound.png', upload_to='web_images/order')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.TextField()),
                ('total_price', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='orderid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='store.orderid'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
