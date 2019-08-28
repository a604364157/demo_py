from django.db import models


class Student(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=20, default='')
    age = models.PositiveSmallIntegerField()


class TwoColorBall(models.Model):
    id = models.BigAutoField
    red1 = models.CharField(max_length=2)
    red2 = models.CharField(max_length=2)
    red3 = models.CharField(max_length=2)
    red4 = models.CharField(max_length=2)
    red5 = models.CharField(max_length=2)
    red6 = models.CharField(max_length=2)
    blue = models.CharField(max_length=2)
    run_date = models.DateField
