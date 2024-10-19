from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):

    posts = Post.objects.all()
    postfrom = PostForm(request.GET)
    if postfrom.is_valid():
        postfrom.save()
        return redirect('test')
    
    
    context = {'posts': posts,
               'form': postfrom}


    return render(request, 'template_1.html', context=context)

