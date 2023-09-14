from django.contrib import admin

# Register your models here.
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","user_phone", "user_profile", "user_address", "user_gender", "slug" )


class Product_IdAdmin(admin.ModelAdmin):
    list_display = ("id", "product_id",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_id", "category_name","product_name","product_image","product_description","product_rating","product_price","product_discount","slug",)
    prepopulated_fields = {"slug": ("product_name",)}


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(Product_Id, Product_IdAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
