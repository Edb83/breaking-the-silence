from django.urls import path
from . import views

urlpatterns = [
    path('profiles/<str:username>/', views.user_profile, name='user_profile'),
    path('edit/', views.edit_user_profile, name='edit_user_profile'),
]
