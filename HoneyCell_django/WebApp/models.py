from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __unicode__(self):
        return "%s wrote %s" %(self.user, self.title)

