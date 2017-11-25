# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag
from mode.models import Mode
from jsonfield import JSONField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    modes = models.ManyToManyField(Mode, blank=True, null=True)
    location_count = JSONField(default={}, blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def update_count(self, location):
        try:
            self.location_count[location] += 1
        except:
            self.location_count[location] = 1
        self.save()
