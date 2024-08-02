from django.conf import settings
from django.db import models
from django.utils import timezone

class Image(models.Model):
    url = models.URLField()
    hashtag = models.CharField(max_length=100)