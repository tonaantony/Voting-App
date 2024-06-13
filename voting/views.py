from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Post, Vote, Candidate
from .forms import VoteForm

def index(request):
    return render(request, 'voting/index.html')

def vote_post(request, post_id=None):
    if post_id is None:
        # Start voting from the first post
        first_post = Post.objects.first()
        if not first_post:
            return redirect('index')
        return redirect('vote_post', post_id=first_post.id)
    
    post = get_object_or_404(Post, id=post_id)
    next_post = Post.objects.filter(id__gt=post_id).first()
    
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
            if next_post:
                return redirect('vote_post', post_id=next_post.id)
            else:
                return render(request, 'voting/vote_complete.html')
    else:
        form = VoteForm(post=post)
    return render(request, 'voting/vote.html', {'post': post, 'form': form, 'next_post': next_post})

@user_passes_test(lambda u: u.is_superuser)
def results(request):
    posts = Post.objects.all()
    return render(request, 'voting/results.html', {'posts': posts})

@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    posts = Post.objects.all()
    return render(request, 'voting/manage.html', {'posts': posts})
