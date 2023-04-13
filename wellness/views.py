from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Wellness
from .forms import CheckinForm
from django.urls import reverse


@login_required
def user_check_in(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            wellness = form.save(commit=False)
            wellness.user = request.user
            wellness.save()
            return HttpResponseRedirect(reverse('wellness_tracker'))
    else:
        form = CheckinForm()
    return render(request, 'wellness/checkin.html', {'form': form})

@login_required
def wellness_tracker(request):
    serialized_stats = []
    serialized_date = []
    for stat in Wellness.objects.filter(user=request.user):
        serialized_stats.append(int(
            stat.health_rating,
        ))
        date_only = stat.date.date()
        serialized_date.append(str(
            date_only
        ))
    serialized_stats.reverse()
    serialized_date.reverse()
    context = {
        "stats": serialized_stats,
        "date": serialized_date
        }
    return render(request, 'wellness/tracker.html', context)

