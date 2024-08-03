from django.contrib import admin
from products.models import *
# Register your models here.
@admin.register(Product,ProductAdditionalInfo,ProductCategory,ProductColor,ProductImage,ProductReview,ProductSubCategory,UserProductFavorite)
class Admin(admin.ModelAdmin):
    pass