from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=60) # Field name made lowercase.
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    organization = models.CharField(max_length=30L, null=True)
    phone = models.CharField(max_length=20L, null=True)
    country = models.ForeignKey(Country)
    affiliation = models.CharField(max_length=20L, null=True)
    img = models.ImageField(blank=True, upload_to='avatar', default='/static/img/profile_picture.png')
    
    def __unicode__(self):
        return self.user.get_full_name()
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Partner(models.Model):
    name = models.CharField(max_length=60) # Field name made lowercase.
    logo = models.ImageField(blank=False, upload_to='/', default='no_disponible.jpg')
    country = models.CharField(max_length=60) # Field name made lowercase.
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Added in")
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
