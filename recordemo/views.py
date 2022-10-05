from django.shortcuts import render
from .models import AddFeeling  # use AddFeeling model in views
from recordemo.forms import AddFeelingForm

# Create your views here.


def RecordEmo(request):
    feelings = AddFeeling.objects.all()

    context = {
        'form': AddFeelingForm(),
    }

    return render(request, 'recordemo/recordemo.html', context)
