from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    related_tags = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.title

# class TagStatus(models.Model):
#     tag = models.ForeignKey(Tag)
# To develop
