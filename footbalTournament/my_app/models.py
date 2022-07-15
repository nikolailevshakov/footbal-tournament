from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    season_points = models.IntegerField()
    month_points = models.IntegerField()
    week_points = models.IntegerField()
