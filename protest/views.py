from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Profile, Post
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from chartit import PivotChart, PivotDataPool
# Create your views here.


def index_profile(request):
    all_profiles = Profile.objects.all()
    context = {'all_profiles':all_profiles}
    return render(request, 'protest/index_profile.html', context)


def detail_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    context = {'profile':profile}
    return render(request, 'protest/detail_profile.html', context)



def index_post(request):
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'protest/index_post.html', context)


def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'protest/detail_post.html', context)


