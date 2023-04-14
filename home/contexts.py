from connections.models import ConnectionRequest

def connect_context(request):
    if request.user.is_authenticated:
        connection_requests = ConnectionRequest.objects.filter(
            receiver=request.user,
            status=0
            )
    else:
        connection_requests = []
    
    context = {
        'connection_requests': connection_requests,
    }

    return context