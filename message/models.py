from django.db import models

# Create your models here.

class GuestUser(models.Model):
    name =models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ({self.ip_address})"

class Message(models.Model):
    sender = models.ForeignKey(GuestUser, on_delete=models.CASCADE, related_name='messages', blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender}: {self.body[:20]}..."