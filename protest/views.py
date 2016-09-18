from django.shortcuts import render
from .models import Profile, Post
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Profile
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

# Create your views here.

'''
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

'''


class IndexViewPost(generic.ListView):
    template_name = 'protest/index_post.html'
    context_object_name = 'all_posts'
    def get_queryset(self):
        return Post.objects.all()

class DetailViewPost(generic.DetailView):
    model = Post
    template_name = 'protest/detail_post.html'

class IndexViewProfile(generic.ListView):
    template_name = 'protest/index_profile.html'
    context_object_name = 'all_profiles'
    def get_queryset(self):
        return Profile.objects.all()

class DetailViewProfile(generic.DetailView):
    model = Profile
    template_name = 'protest/detail_profile.html'

class PostCreate(CreateView):
    model = Post
    fields=['profile_id','subject', 'description', 'organizing_committee', 'age_group', 'incident', 'tag', 'concerned_authority','picture']

class PostUpdate(UpdateView):
    model = Post
    fields=['profile_id','subject', 'description', 'organizing_committee', 'age_group', 'incident', 'tag', 'concerned_authority','picture']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('protest:index_post')

class UserFormView(View):
    form_class = UserForm
    template_name = 'protest/registration_form.html'

    #display a blank form for a new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #register and add user to the db
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # clean and normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if the credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #request.user for later purpose
                    #now redirect them to the home page
                    return redirect('protest:index_post')

        return render(request, self.template_name, {'form': form})

