from django.db import models

# Create your models here.
class Recipe(models.Model):
    recepiName = models.CharField(max_length=70, blank=False, default='')
    recepiDesc = models.CharField(max_length=200, blank=False, default='')
