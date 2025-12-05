from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone
from django.db.models import Sum
# Create your models here.


class NoticePost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    iamge = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def  get_time_difference(obj):
        # now = timezone.now()
        # diff = timesince(obj, now)
        # return f'{timesince(obj.created_at)} ago'
        diff = timesince(obj.created_at).split(',')[0]
        return f'{diff} ago'

    def __str__(self):
        return self.title

class BefaqResultDetails(models.Model):
    class_name = models.CharField(max_length=100)
    students = models.PositiveIntegerField(null=True, blank=True)
    stand = models.PositiveIntegerField(null=True, blank=True)
    stare = models.PositiveIntegerField(null=True, blank=True)
    first_department = models.PositiveIntegerField(null=True, blank=True)
    second_department = models.PositiveIntegerField(null=True, blank=True)
    third_department = models.PositiveIntegerField(null=True, blank=True)
    rasib = models.PositiveIntegerField(null=True, blank=True)
    percent_of_successful = models.CharField(max_length=6)
    year = models.IntegerField(null=True, blank=True)
    merit_place = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Befaq Result Detail'
        verbose_name_plural = 'Befaq Result Details'

    
    def __str__(self):
        return f"{self.class_name} ({self.year})"

    @property
    def sum_stand(self):
        total = BefaqResultDetails.objects.filter(year=self.year).aggregate(total=Sum('stand'))['total']
        return total or 0
    

    @property
    def display_title(self):
        return f"{self.year} সালে {self.sum_stand} জন স্ট্যান্ড করেছে এবং {self.place_of_medal}ম স্থান অর্জন করেছে।"

    
    

