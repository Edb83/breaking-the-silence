from django.shortcuts import render, get_object_or_404, redirect
from .models import ConnectionRequest

def handle_connection(request, connection_id, decision):
    connection_request = get_object_or_404(ConnectionRequest, pk=connection_id)
    if decision == 'accept':
        connection_request.accepted = True
    if decision == 'dismiss':
        connection_request.dismissed = True
    connection_request.save()

    return redirect('user_profile', request.user.username)

