from django.shortcuts import render
from .models import Topic, Post
from django.contrib.auth.decorators import login_required

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'forum/topics.html', {'topics': topics})

@login_required
def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    posts = Post.objects.filter(topic=topic)
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})

