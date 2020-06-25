from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm

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

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None) # When the QueryDict request.POST is empty, it takes a Falsy value
    if form.is_valid():
        obj = form.save(commit=False) #to modify obj later and not dump it right now
        # do other form related logic
        obj.save()
        form = TweetForm() # to return blank form after request handle
    return render(request=request, template_name="components/form.html", context={"form": form})

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