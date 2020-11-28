from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'created_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
