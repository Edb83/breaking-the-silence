from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_user_profile, name='edit_user_profile'),
]
