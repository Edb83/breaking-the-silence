from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from .models import Connection, Conversation, Message
import json


@login_required
def connections(request):
    query = Q(receiver=request.user) | Q(sender=request.user)
    connections = Connection.objects.filter(query)

    context = {
        'pending_requests': connections.filter(status=0),
        'accepted_requests': connections.filter(status=1),
        'dismissed_requests': connections.filter(status=2),
    }

    return render(request, 'connections/connections.html', context)
    

@login_required
def handle_connection(request, connection_id, decision):
    connection_request = get_object_or_404(Connection, pk=connection_id)
    connection_request.status = decision
    connection_request.save()

    return redirect('connections')


@login_required
def create_connection(request, username):
    receiver = get_object_or_404(User, username=username)
    existing_request = Connection.objects.filter(sender=receiver)
    if existing_request.exists():
        existing_request = existing_request.first()
        existing_request.status = 1
        existing_request.save()
        print('existing connection accepted, no new request created')
    else:
        Connection.objects.create(
            sender=request.user,
            receiver=receiver,
        )
        print('new request made')

    return redirect('connections')


@login_required
def all_conversations(request):
    connections = Connection.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    conversations = Conversation.objects.filter(connection__in=connections)

    context = {
        'conversations': conversations,
    }

    return render(request, 'connections/conversations.html', context)


@login_required
def send_message(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    body_string = request.body.decode("utf-8")
    data = json.loads(body_string)
    if request.method == 'POST':
        message = Message.objects.create(
                sender=request.user,
                conversation=conversation,
                content=data.get('comment')
            )
        data = {
            'comment': message.content,
            'created_on': message.created_at.strftime("%H:%M, %d %b")
        }

        return JsonResponse(data)
