from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    tags = models.ManyToManyFilter(Tag)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

