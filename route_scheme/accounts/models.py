# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag
from mode.models import Mode
from jsonfield import JSONField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    tags = models.ManyToManyField(Tag)
    modes = models.ManyToManyField(Mode)
    location_count = JSONField()

    def __unicode__(self):
        return self.user.username

    def update_count(self, location):
        try:
            self.location_count[location] += 1
        except:
            self.location_count[location] = 1
        self.save()
