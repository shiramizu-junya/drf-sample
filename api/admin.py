from django.contrib import admin
from .models import Product, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.index_title = "管理サイトへようこそ"
admin.site.site_header = "管理サイト"
