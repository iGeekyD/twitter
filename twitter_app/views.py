from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    print (args, kwargs)
    return HttpResponse("<h1>Hello Worlds </h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print (args, kwargs)
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse(f"<h1>Tweet {tweet_id}: {obj.content} </h1>")