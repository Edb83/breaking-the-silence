from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Post
from .forms import TopicForm, PostForm, CommentForm
from django.db.models import Q
from django.contrib import messages

def topics(request):
    topics = Topic.objects.all()
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.created_by = request.user  # Corrected line
            new_topic.save()
            messages.success(request, "Thanks for adding a topic!")
            return redirect('topics')
    elif request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter search criteria")
                return render(request, 'forum/topics.html')
            queries = Q(title__icontains=query)
            serialized_topics = topics.filter(queries)
            return render(request, 'forum/topics.html', {'topics': serialized_topics, 'form': form})
    return render(request, 'forum/topics.html', {'topics': topics, 'form': form})

@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.topic = topic
            new_post.created_by = request.user
            new_post.save()
            messages.success(request, "Thanks for adding a post!")
            return redirect('topic_detail', topic_id=topic_id)
    else:
        form = PostForm()
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.created_by = request.user
            new_comment.save()
            messages.success(request, "Thanks for commenting!")
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments, 'form': form})


