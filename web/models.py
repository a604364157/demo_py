from django.db import models


class Student(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=20, default='')
    age = models.PositiveSmallIntegerField()
