from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

from random import randint
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request=request, template_name="pages/home.html", context={}, status=200)

def tweet_list_view (request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id" : x.id , "content" : x.content, "likes" : randint(0, 12)} for x in qs]
    data = {
        "isUser" : False,
        "response" : tweets_list
    }
    return JsonResponse(data=data, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id" : tweet_id,
    }
    status = 200
    try:
        obj: Tweet = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not found'
        status = 404

    return JsonResponse(data=data, status=status)