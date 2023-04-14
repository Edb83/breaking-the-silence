from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Topic, Post
from .forms import TopicForm, PostForm, CommentForm

def topics(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.created_by = request.user  # Corrected line
            new_topic.save()
            return redirect('topics')
    else:
        form = TopicForm()
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
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@user_passes_test(lambda u: u.is_staff)
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm(instance=topic)
    return render(request, 'forum/edit_topic.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.created_by:
        return HttpResponseForbidden("You don't have permission to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', topic_id=post.topic.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/edit_post.html', {'form': form})
