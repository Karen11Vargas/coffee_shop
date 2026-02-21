from django.contrib import admin
from .models import Orders, OrderProduct


# Register your models here.

class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = OrderProduct
    inlines =[
        OrderProductInlineAdmin
    ]

admin.site.register(Orders, OrderAdmin)

