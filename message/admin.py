from django.contrib import admin
from .models import Message
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'created_at']
    search_fields = ['body']
    list_filter = ['created_at']
    ordering = ['-created_at']
    readonly_fields = ['created_at']