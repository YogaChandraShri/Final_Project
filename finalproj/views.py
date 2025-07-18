from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def detail(request):
    return render(request, 'shop-detail.html')

def listing(request):
    return render(request, 'shop-listing.html')
