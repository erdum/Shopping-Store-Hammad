from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    user_gender = models.CharField(max_length=10, default="Select an option")
    user_address = models.TextField(max_length=300, default="")
    user_phone = models.TextField(max_length=15, blank=True, null=True)
    user_profile = models.ImageField(upload_to="web_images", default="web_images/defaultpf.jpg")
    slug = models.SlugField(unique=True, null=True)


class Banner(models.Model):
    image = models.ImageField(upload_to="web_images/store/banner", default="web_images/store/E-Commerce Facebook Ad.png")


class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.category

    class Meta:
        ordering = ['category']


class Product_Id(models.Model):
    product_id = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.product_id 


class Product(models.Model):
    product_id = models.OneToOneField(Product_Id, on_delete=models.CASCADE, related_name="product")
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_name")
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to="web_images/store", default="web_images/store/imagenotfound.png")
    product_description = models.TextField(max_length=100, default="Description not available")
    product_rating = models.FloatField(max_length=10)
    product_price = models.FloatField(max_length=10)
    product_discount = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self) -> str:
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


class Order(models.Model):
    orderid = models.CharField(max_length=200, null=True, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    complete = models.BooleanField(default=False)
    # sub_total = models.IntegerField()
    # shipping_charges = models.IntegerField()
    # total_price = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)

    def get_sub_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    def get_shipping_charges(self):
        shippingCharges = 50
        return shippingCharges

    def get_total(self):
        total = self.get_sub_total() + self.get_shipping_charges()
        return total

    def get_total_items(self):
        orderitems = self.orderitem_set.all()
        count = 0
        for orderitem in orderitems:
            count += 1
        
        return count


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=15)
