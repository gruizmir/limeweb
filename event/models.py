from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from opportunity.models import Opportunity
from smart_selects.db_fields import ChainedForeignKey

class Event(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=100L, blank=False)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100L, blank=False)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    start_date = models.DateTimeField(verbose_name="Last modification")
    end_date = models.DateTimeField(blank=True, verbose_name="Last modification")
    opportunity = models.ForeignKey(Opportunity, null=True)
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
