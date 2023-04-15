from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Connection(models.Model):
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


@receiver(post_save, sender=Connection)
def create_conversation(sender, instance, created, **kwargs):
    if instance.status == 1:
        Conversation.objects.get_or_create(connection=instance)
    # instance.conversation.save()


class Conversation(models.Model):
    connection = models.OneToOneField(Connection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversation {self.id}'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message {self.id} from {self.sender}'

    class Meta:
        ordering = ['created_at']
