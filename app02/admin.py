from django.contrib import admin

# Register your models here.
from app02.models import Publication, Member
admin.site.register(Publication)
admin.site.register(Member)
