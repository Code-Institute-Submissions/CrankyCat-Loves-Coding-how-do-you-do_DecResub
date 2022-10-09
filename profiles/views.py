from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .form import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'

    context = {
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def edit_profile(request, user_id):

    profile = get_object_or_404(UserProfile, user=user_id)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    form = UserProfileForm(instance=profile)

    context = {
        
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)
