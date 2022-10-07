from django.shortcuts import render, redirect
from .models import AddFeeling
from recordemo.forms import AddFeelingForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def RecordEmo(request):

    if request.method == 'POST':
        form = AddFeelingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emobox/emobox.html')
            form = AddFeelingForm()
    else:
        form = AddFeelingForm

    # template = 'recordemo/recordemo.html'

    # if request.method == 'POST':
    #     form = AddFeelingForm(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         form.save() 
    #         return redirect('emobox/emobox.html')
    # form = AddFeelingForm()

    context = {
        'form': AddFeelingForm(),
    }

    return render(request, 'recordemo/recordemo.html', context)
