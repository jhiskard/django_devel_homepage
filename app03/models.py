from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.

SAMPLE_CLASS =\
"""
class DjangoBoard(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateField(null=True, blank=True)
    mail = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=200, blank=True)
    hits = models.IntegerField(null=True, blank=True)
"""

class BoardModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    serial = models.IntegerField(null=True, blank=True)
    title  = models.CharField(max_length=200, blank=True)
    contents  = models.TextField(max_length=10000, blank=True)
    created   = models.DateTimeField(default=now)
    modified  = models.DateTimeField(auto_now=True)
