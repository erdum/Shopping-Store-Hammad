"""
URL configuration for Shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from store.views import *

urlpatterns = [
    path("", home, name="home"),
    path("shop/", Store.as_view(), name="shop"),
    path("shop/products/<slug>", ProductDetailView.as_view(), name="product_detail"),
    path("shop/cart/", cart_page, name="cart_page"),

    # Paths for cart functionality:
    path("update_item/", update_item, name="update_item"),
    # Path for order processing:
    path("process_order/", process_order, name="process_order"),



    path("shop/products/checkout/", checkout_page, name="checkout_page"),
    path("profile/<slug>/", profile, name="profile"),
    path("login/", login_view, name="login_view"),
    path("signup/", signup_view, name="signup_view"),
    path("logout/", logout_view, name="logout_view"),
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()


