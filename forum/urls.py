from django.urls import path
from . import views

urlpatterns = [
    path('', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('topic/<int:topic_id>/edit/', views.edit_topic, name='edit_topic'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/reported/', views.reported, name='reported'),
]