from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import AddFeeling
from recordemo.forms import AddFeelingForm

from profiles.models import UserProfile
from profiles.form import UserProfileForm


@login_required
def RecordEmo(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    
    if request.method == 'POST':
        form = AddFeelingForm(request.POST)

        if form.is_valid():
            form.instance.user_profile = profile
            form.save()
            return redirect('recordemo')
    else:
        form = AddFeelingForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'recordemo/recordemo.html', context)