from django.contrib import admin
from .models import NoticePost
# Register your models here.


@admin.register(NoticePost)
class NoticePostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'created_at', 'updated_at', 'get_time_difference']