from connections.models import Connection, Conversation
from django.db.models import Q

def convo_context(request):
    conversations = []
    if request.user.is_authenticated:
        connections = Connection.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
        conversations = Conversation.objects.filter(connection__in=connections)

    context = {
        'conversations': conversations,
    }
    return context

