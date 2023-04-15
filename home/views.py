from django.shortcuts import render
from forum.models import Topic

def home(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'home/home.html', context)