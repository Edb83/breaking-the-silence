from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Wellness
from .forms import CheckinForm

def user_check_in(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/wellness/')
    else:
        form = CheckinForm()
    return render(request, 'checkin.html', {'form': form})
