from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ConnectionRequest



@login_required
def handle_connection(request, connection_id, decision):
    connection_request = get_object_or_404(ConnectionRequest, pk=connection_id)
    if decision == 'accept':
        connection_request.accepted = True
    if decision == 'dismiss':
        connection_request.dismissed = True
    connection_request.save()

    return redirect('user_profile', request.user.username)


@login_required
def create_connection(request, username):
    receiver = get_object_or_404(User, username=username)
    connection, created = ConnectionRequest.objects.get_or_create(
        sender=request.user,
        receiver=receiver,
    )
    if created:
        # messages sent
        pass
    else:
        # messages already sent
        pass

    return redirect('user_profile', request.user.username)