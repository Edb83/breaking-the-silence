from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    FORCES_CHOICES = (
        ('army', 'Army'),
        ('navy', 'Navy'),
        ('air_force', 'Air Force'),
        ('marines', 'Marines'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    story = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)
    force = models.CharField(max_length=50, choices=FORCES_CHOICES, null=True, blank=True)
    regiment = models.CharField(max_length=100, null=True, blank=True)
    rank = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

