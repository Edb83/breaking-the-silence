from connections.models import ConnectionRequest

def connect_context(request):
    connection_requests = ConnectionRequest.objects.filter(
        receiver=request.user,
        accepted=False,
        dismissed=False
        )
    
    context = {
        'connection_requests': connection_requests,
    }

    return context