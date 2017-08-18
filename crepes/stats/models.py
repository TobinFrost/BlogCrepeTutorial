from __future__ import unicode_literals

from django.db import models

class Page(models.Model):
    url = models.URLField()
    visites = models.IntegerField(default=1)

    def __str__(self):
        return u"[{0}]".format(self.url)

# Create your models here.
