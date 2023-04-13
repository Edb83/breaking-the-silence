from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    display_username = "Anonymous" if user_profile.is_anonymous else user_profile.user.username
    context = {'user_profile': user_profile, 'display_username': display_username}
    return render(request, 'user_profile.html', context)


