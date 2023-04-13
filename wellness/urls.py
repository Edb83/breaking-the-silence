from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_check_in, name='user_check_in'),
    path('tracker', views.wellness_tracker, name='wellness_tracker'),
]
