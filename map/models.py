from django.db import models


class Well(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    information = models.TextField(null=False, blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    thumbnailImage = models.TextField()
    extraImages = models.TextField()

    def __str__(self):
        return self.name
