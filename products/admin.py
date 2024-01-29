from django.contrib import admin
from .models import Product, Category, Brand, HeatLevel

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'heat_level',
        'category',
        'price',
        'rating',
    )
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class HeatLevelAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'heat_order',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(HeatLevel, HeatLevelAdmin)