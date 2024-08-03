from django.conf import settings
from django.db import models
from django.utils import timezone

class Image(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now, editable = False)

    def __str__(self):
        return self.url