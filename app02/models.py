from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.

def upload_path_handler(instance, filename):
    name = "papers_thumbnail/{year}/{file}".format(
    year=instance.year, file=filename)
    return name

class Publication(models.Model):
    thumbnail = models.ImageField(upload_to=upload_path_handler, blank=True)
    title = models.TextField(max_length=200)
    authors = models.TextField(max_length=200)
    journal = models.TextField(max_length=200)
    year = models.IntegerField()
    vol  = models.IntegerField()
    issue = models.IntegerField(blank=True, null=True)
    pages = models.TextField(max_length=200)
    doi =   models.TextField(max_length=200, blank=True)
    link =  models.TextField(max_length=1000, blank=True)
    abstract = models.TextField(max_length=50000, blank=True)
    published_month = models.IntegerField(blank=True, null=True)
    published_date =  models.IntegerField(blank=True, null=True)

