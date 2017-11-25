from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField
# Create your models here.

class Mode(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    extra_fields = JSONField()

    def __unicode__(self):
        return self.name
