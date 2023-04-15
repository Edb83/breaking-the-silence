from django.urls import path
from . import views

urlpatterns = [
    path('connections/', views.connections, name='connections'),
    path('connect/<str:username>/', views.create_connection, name='create_connection'),
    path('handle/<int:connection_id>/<str:decision>/', views.handle_connection, name='handle_connection'),
    path('conversations/', views.all_conversations, name='conversations'),
]