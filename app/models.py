from django.db import models
from datetime import date
# Create your models here.
class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    upload_to = 'file/{0}/{1}'.format(date.today().year, date.today().month)
    fileUpload = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.title
