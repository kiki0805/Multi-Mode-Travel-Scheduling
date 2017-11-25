from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField
# Create your models here.

class Mode(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=255)
    extra_fields = JSONField()
    # {
    # 'duration': {
    #   'weight': ,
    #   'value': , 
    # },
    # 'begin_time': {
    #   'weight': ,
    #   'value': ,
    #  }, 
    # 'end_time': {
    #   'weight': ,
    #   'value': ,
    # },
    # 'come_over_locations': {
    #   'weight': ,
    #   'value': ,
    # }}

    def __unicode__(self):
        return self.name
