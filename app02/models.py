from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.

def upload_path_handler(instance, filename):
    name = "papers_thumbnail/{year}/{file}".format(
    year=instance.year, file=filename)
    return name

class Publication(models.Model):
    priority  = models.IntegerField(default=0)
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


SORT_OF_STATUS = (
                  ("Research Staff", "Research Staff"),
                  ("Students", "Students"),
                  ("Staff", "Staff"),
                 )

SORT_OF_DEGREE = (
                  ("Research Professor", "Research Professor"),
                  ("Ph.D. Candidate", "Ph.D. Candidate"),
                  ("M.S. Candidate", "M.S. Candidate"),
                  ("Graduate Research Assistant", "Graduate Research Assistant"),
                  ("Secretary", "Secretary"),
                 )

SORT_OF_ENDING = (
                  ("Postdoc.", "Postdoc."),
                  ("Ph.D.", "Ph.D."),
                  ("M.S.", "M.S."),
                  ("B.S.", "B.S."),
                  ("Co-advised", "Co-advised"),
                 )

def upload_path_handler_member(instance, filename):
    name = "members_thumbnail/{name}/{file}".format(
    name=instance.name, file=filename)
    return name

class Member(models.Model):
    # for current members
    priority  = models.IntegerField(default=0)
    name   = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to=upload_path_handler_member, 
                                  blank=True)
    status = models.CharField(max_length=50, choices=SORT_OF_STATUS, 
                              default="Students", blank=True)
    degree = models.CharField(max_length=50, choices=SORT_OF_DEGREE, 
                              default="M.S. Candidate", blank=True)
    fields = models.TextField(max_length=200, blank=True, null=True)
    office = models.TextField(max_length=200, blank=True, null=True)
    email  = models.EmailField(blank=True, null=True)
    tel    = models.CharField(max_length=50, blank=True, null=True)
    # for graduate members
    is_graduate     = models.BooleanField(default=False)
    end_as          = models.CharField(max_length=50, choices=SORT_OF_ENDING,
                                       default="M.S.", blank=True, null=True)
    currentposition = models.TextField(max_length=200, blank=True, null=True)


def upload_path_handler_news(instance, filename):
    name = "news_attached/{datetime}/{file}".format(
    datetime=instance.datetime, file=filename)
    name1 = name.split()[0]; name2 = name.split()[1]
    return name1 + '_' + name2

class News(models.Model):
    priority = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=now)
    endtime  = models.DateTimeField(blank=True, null=True)
    contents = models.TextField(max_length=5000, blank=True)
    attached = models.ImageField(upload_to=upload_path_handler_news, blank=True)
    is_activ = models.BooleanField(default=True)

