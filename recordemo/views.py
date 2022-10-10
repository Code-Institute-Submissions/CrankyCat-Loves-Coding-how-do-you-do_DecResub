from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import AddFeeling
from recordemo.forms import AddFeelingForm

from profiles.models import UserProfile
from profiles.form import UserProfileForm


# @login_required
# # def RecordEmo(request, user_id):
# def RecordEmo(request):

#     # profile = get_object_or_404(UserProfile, user=user_id)
#     # print(profile)
#     form = AddFeelingForm()

#     if request.method == 'POST':
#         # form = AddFeelingForm(request.POST, instance=profile)
#         form = AddFeelingForm(request.POST)

#         if form.is_valid():
#             print(form)
#             form.save()
#             # form = AddFeelingForm(instance=profile)
#             form = AddFeelingForm()

#     context = {
#         # 'profile': profile,
#         'form': form,
#     }

#     return render(request, 'recordemo/recordemo.html', context)


@login_required
def RecordEmo(request):

    form = AddFeelingForm()

    if request.method == 'POST':
        form = AddFeelingForm(request.POST)

        if form.is_valid():
            form.save()
            form = AddFeelingForm()

    context = {
        'form': form,
    }

    return render(request, 'recordemo/recordemo.html', context)
