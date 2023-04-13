from django.urls import path
from . import views

urlpatterns = [
    path('handle/<int:connection_id>/<str:decision>', views.handle_connection, name='handle_connection'),
]