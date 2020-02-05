from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Posts,Category,PostsForm
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def posts(request,pk=None):
    if request.method=="POST":
        post=PostsForm(request.POST,request.FILES)
        
        if(post.is_valid()):
            post.save()
            post={
                'message':"Your data is successfully submited ",
            
            }
        else:
            post={
                'message':"You enterd wrong data",
                "error":post.errors.as_json()
            }
        posts=json.dumps(post)
    else:
        if pk is None:
            posts=Posts.objects.all()
        else:
            posts=Posts.objects.filter(pk=pk)
            posts=serialize('json',posts,fields=('title','content','thumbnail','user','category'),use_natural_foreign_keys=True)   
    
    
    return HttpResponse(posts,content_type='application/json')

# Create your views here.
