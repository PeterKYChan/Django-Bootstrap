from django.db import models
from django.db import models
from django.contrib import admin

# Create your models here.
class Experiment(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 2000)
    csv = models.TextField()
    files = models.FileField(upload_to = "media")

    def __unicode__(self):
        return self.name

admin.site.register(Experiment)
