from django.db import models

from artists.models import Artist

class Album(models.Model):
    title = models.CharField(max_length=225)
    cover = models.ImageField(upload_to='albums')
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.title
