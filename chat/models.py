from django.db import models

class chat_message(models.Model):
    role = models.CharField(max_length=30)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)