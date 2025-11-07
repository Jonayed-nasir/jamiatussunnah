from django.contrib import admin
from .models import NoticePost, BefaqResultDetails
# Register your models here.


@admin.register(NoticePost)
class NoticePostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'created_at', 'updated_at']

@admin.register(BefaqResultDetails)
class BefaqResultDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'students', 'stand', 'stare', 'first_department', 'second_department', 'third_department', 'rasib', 'percent_of_successful', 'year', 'merit_place', 'sum_stand', 'display_title']