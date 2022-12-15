from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import AddFeeling
from recordemo.forms import AddFeelingForm

from profiles.models import UserProfile
from profiles.form import UserProfileForm


@login_required
def add_emo(request):
    """function for user to add emo"""

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


@login_required
def update_emo(request, pk):
    """function allows user to edit an emo"""

    emo = AddFeeling.objects.get(pk=pk)
    form = AddFeelingForm(request.POST or None, instance=emo)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Emo updated successfully!'
            )
            return redirect('show_emo')
        else:
            messages.error(
                request,
                (
                    'Failed to update Emo. '
                    'Please try later.'
                )
            )
    else:
        messages.info(
            request,
            'You are editing an emo'
        )

    context = {
        'form': form,
        'emo': emo,
    }

    return render(request, 'recordemo/recordemo.html', context)


@login_required
def delete_emo(request, pk):
    """function allows user to edit an emo"""

    emo = get_object_or_404(AddFeeling, pk=pk)
    user = get_object_or_404(UserProfile, user=request.user)
    emo.delete()
    messages.success(
        request,
        'Emo deleted successfully!'
    )
    return redirect(reverse('emobox', args=[user.user_id]))
