from django.db import models

# Create your models here.
class Report(models.Model):
    tipo = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    time = models.DateTimeField()
    image = models.ImageField(upload_to='report_images')
