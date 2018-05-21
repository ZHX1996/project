from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.
def userdemo(request):
    desc = User.objects.all()[0]
    return HttpResponse(desc)

