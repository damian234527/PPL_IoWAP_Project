from django.db import models

# Create your models here.


class Message(models.Model):
    content = models.TextField()
    creator = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
