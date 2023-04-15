from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Topic, Post, Comment
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
            new_topic.created_by = request.user  
            new_topic.save()
            messages.success(request, "Thanks for adding a topic!")
            return redirect('topics')
    elif request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter search criteria")
                return redirect(reverse('topics'))
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
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.filter(parent=None)

    parent_comment_id = request.GET.get('parent')
    if parent_comment_id:
        parent_comment = get_object_or_404(Comment, id=parent_comment_id)
    else:
        parent_comment = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.id]))
    else:
        if parent_comment:
            form = CommentForm(initial={'parent': parent_comment})
        else:
            form = None

    context = {'post': post, 'comments': comments, 'form': form, 'parent_comment': parent_comment}
    return render(request, 'forum/post_detail.html', context)

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
