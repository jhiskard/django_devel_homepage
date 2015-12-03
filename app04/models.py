from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

def upload_path_handler(instance, filename):
    name = "structure_files/user_{id}/{created}/{file}".format(
    id=instance.user.id, created=str(instance.created).replace(':','_').replace('+','_'), file=filename)
    name1 = name.split()[0]; name2 = name.split()[1]
    return name1 + '_' + name2

class StructureModel(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    structure = models.FileField(upload_to=upload_path_handler)
    description = models.TextField(max_length=5000, blank=True)
    commands = models.TextField(max_length=10000, blank=True, 
                                default="""# Your initial structure was already loaded in "atoms", i.e, 
# atoms = io.read_xyz('your file')
# After manipulation, the final name of your AtomsSystem object should be "atoms".
""")
    created  = models.DateTimeField(default=now)

