from django.contrib import admin
from .models import Message, GuestUser
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'body', 'created_at']
    search_fields = ['body']
    list_filter = ['created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at']

@admin.register(GuestUser)
class GuestUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at']