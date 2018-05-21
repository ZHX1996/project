from django.shortcuts import render

def index(request):
    return render(request,'index.html', {'images':'1.jpg'})
# Create your views here.
