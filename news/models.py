from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField("Name", max_length=255)

    def __unicode__(self):
        return self.name

class New(models.Model):
    title = models.CharField("Title", max_length=255)
    body  = models.TextField("News Body")
    user  = models.ForeignKey(User)
    created_at = models.DateTimeField("Created at", auto_created=True)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title


admin.site.register(New)
admin.site.register(Category)
