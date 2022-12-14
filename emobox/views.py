from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recordemo.models import AddFeeling
from recordemo.forms import AddFeelingForm

from profiles.models import UserProfile
from profiles.form import UserProfileForm


def show_emo(request, pk):
    """A view for render single emo details"""

    emo = AddFeeling.objects.get(pk=pk)

    context = {
        'emo': emo,
    }

    return render(request, 'emobox/show_emo.html', context)


@login_required
def EmoBox(request, user_id):
    """ Display individual user's feelings. """

    # get perticular user profile first
    profile = get_object_or_404(UserProfile, user=user_id)

    # then filter all feelings belong to this user
    feelings = profile.user_feelings.all()

    context = {
        'feelings': feelings,
        'profile': profile,
    }

    return render(request, 'emobox/emobox.html', context)


# not functional yet
@login_required
def EditEmoBox(request, user_id):
    profile = get_object_or_404(UserProfile, user=user_id)
    feelings = profile.user_feelings.all().first()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=feelings)
        if form.is_valid():
            form.save()
    form = UserProfileForm(instance=feelings)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'emobox/edit_emobox.html', context)


@login_required
def DeleteEmoBox(request, user_id):
    profile = get_object_or_404(UserProfile, user=user_id)
    feelings = profile.user_feelings.all().first()
    feelings.delete()

    return render(request, 'emobox/delete_emobox.html')