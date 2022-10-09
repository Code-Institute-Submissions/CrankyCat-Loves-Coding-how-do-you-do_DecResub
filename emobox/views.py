from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recordemo.models import AddFeeling
from recordemo.forms import AddFeelingForm

from profiles.models import UserProfile
from profiles.form import UserProfileForm


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
