from django.db import models

# Create your models here.


class Message(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.body[:20]}..."