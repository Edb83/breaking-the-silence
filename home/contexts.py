from connections.models import Connection

def connect_context(request):
    if request.user.is_authenticated:
        connection_requests = Connection.objects.filter(
            receiver=request.user,
            status=0
            )
    else:
        connection_requests = []
    
    context = {
        'connection_requests': connection_requests,
    }

    return context