from django.db import models

from artists.models import Artist
from albums.models import Album

#En models.Model estamos heredando de models que ya existe
class Track(models.Model):
    title = models.CharField(max_length=225)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    album = models.ForeignKey(Album)
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.title
