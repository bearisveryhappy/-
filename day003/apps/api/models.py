from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
