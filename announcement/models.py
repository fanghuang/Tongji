from django.db import models
from django.utils.translation import ugettext_lazy as _


class Announcement(models.Model):
    title = models.CharField(max_length=64, verbose_name=_("Title"))
    time = models.DateTimeField(auto_now_add=True)
    url = models.URLField(verbose_name=_("URL"))

    def __unicode__(self):
        return self.title