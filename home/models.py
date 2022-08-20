from django.db import models

# Create your models here.
#make migration = create changes and store in a file
#migrate - apply the pending changes created by make migration
class Contact(models.Model):
    name = models.CharField( max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    #str representation is shown in the database entry defualt is classobject1 so on
    def __str__(self):
        return self.name

from django.utils import timezone
import os
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Photo(models.Model):

    image = models.ImageField(null=False, blank=False)
    #photo = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)










    
    

