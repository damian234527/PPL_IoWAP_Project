from django.db import models
import os
# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="uploads/")

    def filename(self):
        return os.path.basename(self.file.name)

