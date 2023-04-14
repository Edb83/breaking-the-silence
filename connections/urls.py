from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_connections, name='all_connections'),
    path('create/<str:username>/', views.create_connection, name='create_connection'),
    path('handle/<int:connection_id>/<str:decision>/', views.handle_connection, name='handle_connection'),
]