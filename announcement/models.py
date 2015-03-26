from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
