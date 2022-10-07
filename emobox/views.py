from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from recordemo.forms import AddFeelingForm
from recordemo.models import AddFeeling


# Create your views here.
@login_required
def EmoBox(request):
    
    emobox_feeling = AddFeeling.objects.all()

    context = {
        'emobox_feeling': emobox_feeling,
    }

    
    
    return render(request, 'emobox/emobox.html', context)