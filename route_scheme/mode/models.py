from django.db import models
from tags.models import Tag
from accounts.models import UserProfile
# Create your models here.

class Mode(models.Model):
    name = models.TextField()
    user = models.ForeignKey(UserProfile)
    extra_fields = models.JSONField()

    def __unicode__(self):
        return self.name