from django.contrib import admin
from .models import Admission
# Register your models here.


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'birth_or_nid_card_no', 'father_name','phone_number','occupation', 'father_or_mather_nid_no', 'guardian_phone_number',  'permanent_address_village', 'permanent_address_post_office', 'permanent_address_Upazila', 'permanent_address_district','current_address_village', 'current_address_post_office', 'current_address_Upazila', 'current_address_district', 'guardian_name', 'guardian_phone_number', 'guardian_address', 'Previous_class', 'Where_read', 'current_class', 'created_at')
    search_fields = ('name', 'father_name', 'phone_number')
    list_filter = ('created_at',)