from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def home(request):
    post=Post.objects.all()
    data=serializers.serialize('json',post)
    return HttpResponse(data,content_type='text/json')