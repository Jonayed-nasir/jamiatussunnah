from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class Admission(models.Model):
    name = models.CharField(max_length=100, verbose_name='নাম')
    birth_date = models.DateField(verbose_name='জন্ম তারিখ')
    birth_or_nid_card_no = models.BigIntegerField(verbose_name='জন্ম বা এনআইডি কার্ড নম্বর')
    father_name = models.CharField(max_length=100, verbose_name='পিতার নাম')
    occupation = models.CharField(max_length=200, verbose_name='পেশা')
    mather_name = models.CharField(max_length=100, verbose_name='মাতার নাম')
    father_or_mather_nid_no = models.BigIntegerField(verbose_name='পিতা বা মাতার এনআইডি কার্ড নম্বর')
    phone_number = models.IntegerField(verbose_name='ফোন নম্বর')
    permanent_address_village = models.CharField(max_length=250, verbose_name='স্থায়ী ঠিকানা: গ্রাম')
    permanent_address_post_office = models.CharField(max_length=250, verbose_name='স্থায়ী ঠিকানা: ডাকঘর')
    permanent_address_Upazila = models.CharField(max_length=250, verbose_name='স্থায়ী ঠিকানা: উপজেলা')
    permanent_address_district = models.CharField(max_length=250, verbose_name='স্থায়ী ঠিকানা: জেলা')
    current_address_village = models.CharField(max_length=250, verbose_name='বর্তমান ঠিকানা: গ্রাম')
    current_address_post_office = models.CharField(max_length=250, verbose_name='বর্তমান ঠিকানা: ডাকঘর')
    current_address_Upazila = models.CharField(max_length=250, verbose_name='বর্তমান ঠিকানা: উপজেলা')
    current_address_district = models.CharField(max_length=250, verbose_name='বর্তমান ঠিকানা: জেলা')
    guardian_name = models.CharField(max_length=100, verbose_name='অভিভাবকের নাম')
    guardian_phone_number = models.IntegerField(verbose_name='অভিভাবকের ফোন নম্বর')
    guardian_address = models.CharField(max_length=250, verbose_name='অভিভাবকের ঠিকানা')
    Previous_class = models.CharField(max_length=250, verbose_name='পূর্ববর্তী শ্রেণী') 
    Where_read = models.CharField(max_length=250,verbose_name='কোথায় পড়েছেন')
    current_class = models.CharField(max_length=250, verbose_name='বর্তমান শ্রেণী')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='তৈরির তারিখ')
