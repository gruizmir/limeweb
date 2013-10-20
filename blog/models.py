from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=20L, blank=False)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Blog Categories'
        verbose_name = 'Blog Category'
        

class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=120L, blank=False)
    subtitle = models.CharField(max_length=150L, blank=False)
    body = HTMLField(blank=True)
    category = models.ForeignKey(Category)
    creation_date = models.DateTimeField(auto_now_add=True,)
    mod_date = models.DateTimeField(auto_now=True, verbose_name="Last modification")
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['creation_date']

class Tag(models.Model):
    article = models.ForeignKey(Article)
    tag = models.CharField(max_length=20L, blank=False)
    
