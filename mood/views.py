from django.shortcuts import render

# Create your views here.
def Mood(request):
    return render(request, 'mood/mood.html')


def HowItWork(request):
    return render(request, 'mood/howitworks.html')