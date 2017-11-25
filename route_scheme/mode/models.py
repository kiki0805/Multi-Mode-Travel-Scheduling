from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField


class Mode(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=255)
    extra_fields = JSONField()

    def __unicode__(self):
        return self.name
