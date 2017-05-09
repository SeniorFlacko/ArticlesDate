# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    class Meta:
        ordering = ['pub_date']
    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})