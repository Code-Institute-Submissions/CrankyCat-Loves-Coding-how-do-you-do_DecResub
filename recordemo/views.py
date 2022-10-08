from django.shortcuts import render, redirect
from .models import AddFeeling
from recordemo.forms import AddFeelingForm
from django.contrib.auth.decorators import login_required


# Create your views here.

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
