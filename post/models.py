from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone
# Create your models here.


class NoticePost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    iamge = models.ImageField(null=True)
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

