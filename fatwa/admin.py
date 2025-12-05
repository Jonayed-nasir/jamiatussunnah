from django.contrib import admin
from .models import Category, Fatwa
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Fatwa)
class FatwaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'address', 'question', 'answer', 'reference', 'created_at', 'updated_at']

