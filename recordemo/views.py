from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import AddFeeling
from recordemo.forms import AddFeelingForm

from profiles.models import UserProfile
from profiles.form import UserProfileForm


@login_required
def RecordEmo(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = AddFeelingForm(request.POST)

        if form.is_valid():
            form.instance.user_profile = profile
            form.save()
            messages.success(
                request,
                'Emo added successfully!'
            )
            return redirect('recordemo')
        else:
            messages.error(
                request,
                (
                    'Failed to add Emo. '
                    'Please try later.'
                )
            )
    else:
        form = AddFeelingForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'recordemo/recordemo.html', context)
