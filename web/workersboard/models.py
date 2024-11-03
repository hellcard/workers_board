from typing import Any
from django.db import models

# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'NAME')
    age = models.IntegerField(verbose_name = 'AGE')
    exp = models.FloatField(verbose_name = 'EXPERIENCE')
    date = models.DateTimeField(auto_now_add = True, db_index = True)

    class Meta:
        verbose_name_plural = 'workers'
        verbose_name = 'worker'
        ordering = ['-date']