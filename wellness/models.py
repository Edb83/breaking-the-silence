from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Wellness(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    health_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns a string representation of this model.'''
        return f"{self.user} | {self.date}"
