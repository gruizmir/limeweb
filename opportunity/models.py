from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from main.models import Country
from tinymce.models import HTMLField

class OpCategory(models.Model):
    name = models.CharField(max_length=20L, blank=False)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Opportunity Category"
        verbose_name_plural = "Opportunity Categories"

class Opportunity(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=120L, blank=False)
    description = HTMLField(blank=True)
    target = models.CharField(max_length=150L, blank=False)
    target_description = HTMLField(blank=True)
    institution = models.CharField(max_length=150L, blank=False)
    country = models.ForeignKey(Country)
    amount = models.FloatField(null=True)
    category = models.ForeignKey(OpCategory)
    deadline = models.DateTimeField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True, verbose_name="Last modification")
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['deadline']
        verbose_name_plural = "Opportunities"
