from django.contrib import admin
from orders.models import *
# Register your models here.
@admin.register(Order,Cart,CartItem)
class Admin(admin.ModelAdmin):
    pass
    