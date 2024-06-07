from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Post, Vote, Candidate
from .forms import VoteForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'voting/index.html', {'posts': posts})

def vote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = VoteForm(request.POST, post=post)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            if request.user.is_authenticated:
                vote, created = Vote.objects.get_or_create(
                    voter=request.user,
                    candidate__post=post,
                    defaults={'candidate': candidate}
                )
                if not created:
                    vote.candidate = candidate
                    vote.save()
            else:
                Vote.objects.create(candidate=candidate)
            return redirect('index')
    else:
        form = VoteForm(post=post)
    return render(request, 'voting/vote.html', {'post': post, 'form': form})

@user_passes_test(lambda u: u.is_superuser)
def results(request):
    posts = Post.objects.all()
    return render(request, 'voting/results.html', {'posts': posts})

@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    posts = Post.objects.all()
    return render(request, 'voting/manage.html', {'posts': posts})
