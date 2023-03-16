from django.shortcuts import render

# Create your views here.
def redbus(request):
    return render(request,'redbus.html')
def yellowbus(request):
    return render(request,'yellowbus.html')

