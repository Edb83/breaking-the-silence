from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Wellness
from .forms import CheckinForm

@login_required
def user_check_in(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            wellness = form.save(commit=False)
            wellness.user = request.user
            wellness.save()
            return HttpResponseRedirect('/wellness/tracker')
    else:
        form = CheckinForm()
    return render(request, 'wellness/checkin.html', {'form': form})

