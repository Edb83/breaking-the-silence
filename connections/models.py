from django.db import models
from django.contrib.auth.models import User

class ConnectionRequest(models.Model):
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Accepted'),
        (2, 'Dismissed')
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sender', 'receiver'], name='unique_match')
        ]

    def __str__(self):
        return f'{self.sender} -> {self.receiver}'
