from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255)
    related_tags = models.ManyToManyField("self")


# class TagStatus(models.Model):
#     tag = models.ForeignKey(Tag)
# To develop
