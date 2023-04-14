from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Connection


@login_required
def all_connections(request):
    query = Q(receiver=request.user) | Q(sender=request.user)
    connections = Connection.objects.filter(query)

    context = {
        'pending_requests': connections.filter(status=0),
        'accepted_requests': connections.filter(status=1),
        'dismissed_requests': connections.filter(status=2),
    }

    return render(request, 'connections/all_connections.html', context)
    

@login_required
def handle_connection(request, connection_id, decision):
    connection_request = get_object_or_404(Connection, pk=connection_id)
    connection_request.status = decision
    connection_request.save()

    return redirect('all_connections')


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

    return redirect('all_connections')