from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    privilege = models.IntegerField('privilege')
    def __unicode__(self):
        return self.username
