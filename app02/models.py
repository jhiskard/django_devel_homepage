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


class Member(models.Model):

    # for current members
    thumbnail = models.ImageField(upload_to=upload_path_handler, blank=True)
    name   = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=SORT_OF_STATUS, 
                              default="Students")
    degree = models.CharField(max_length=50, choices=SORT_OF_DEGREE, 
                              default="M.S. Candidate")
    fields = models.TextField(max_length=200, blank=True, null=True)
    office = models.TextField(max_length=200, blank=True, null=True)
    email  = models.EmailField(blank=True, null=True)
    tel    = models.CharField(max_length=50, blank=True, null=True)

    # for graduate members
    is_graduate     = models.BooleanField(default=False)
    end_as          = models.CharField(max_length=50, choices=SORT_OF_ENDING,
                                       default="M.S.")
    currentposition = models.TextField(max_length=200, blank=True, null=True)


