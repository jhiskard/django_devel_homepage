from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.

def upload_path_handler(instance, filename):
    name = "user_{id}/{created}/{file}".format(
    id=instance.user.id, created=instance.created, file=filename)
    name1 = name.split()[0]; name2 = name.split()[1]
    return name1 + '_' + name2

class app01_UploadStructureModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    structurefile = models.FileField(upload_to=upload_path_handler)
    description   = models.TextField(max_length=5000, blank=True)
    commands = models.TextField(max_length=10000, blank=True, 
                                default="""# Your initial structure was already loaded in "atoms", i.e, 
# atoms = io.read_xyz('your file')
# After manipulation, the final name of your AtomsSystem object should be "atoms".
""")
    created  = models.DateTimeField(default=now)


from django.contrib.auth.models import User

class Question(models.Model):
    """question
    when a user posts questions
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return u"{0}".format(self.title)
