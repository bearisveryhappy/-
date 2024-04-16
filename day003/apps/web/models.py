from django.db import models

# Create your models here.
class department(models.Model):
    name = models.CharField(verbose_name='名字',max_length=24)
    position = models.PositiveIntegerField(verbose_name='')
