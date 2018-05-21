from django.shortcuts import render

from django.template import Context, loader
from django.http import HttpResponse
from .models import test

def index(request):
    id = request.GET['id']
    display_list = test.objects.get(id = int(id))
    tmpl = loader.get_template("index.html")
    cont = Context({'test':display_list})
    return HttpResponse(tmpl.render(cont))