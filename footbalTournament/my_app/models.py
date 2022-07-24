from django.db import models
from django.core.validators import MinValueValidator


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    season_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    month_points = models.IntegerField(validators=[MinValueValidator(0)])
    week_points = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name}, {self.email}, points: season {self.season_points}, month {self.month_points}, week {self.week_points}"