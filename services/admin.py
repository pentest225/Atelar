from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CreatArtisan,CreatImage,Service)
class Admin(admin.ModelAdmin):
    pass