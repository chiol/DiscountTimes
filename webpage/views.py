from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webpage/event.html', {})
def event(request):
    return render(request, 'webpage/event.html', {})
def location(request):
    return render(request, 'webpage/location.html', {})
def business(request):
    return render(request, 'webpage/business.html', {})
