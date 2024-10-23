from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def home(request):

    posts = Post.objects.all() #ყველა პოსტის წამოღება
    context = {'posts': posts}

    return render(request, 'template_1.html', context=context)  


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail_post.html', context={'post': post})


def create_post(request):
    postfrom = PostForm()
    if request.method == 'POST':
        postfrom = PostForm(request.POST) # PostForm-ის შევსება request-ში მოსული მონაცემებით
        if postfrom.is_valid(): # მონაცემების ვალიდურობის შემოწმება
            postfrom.save() # ჩანაწერის ბაზაში შენახვა
            return redirect('home') 
    return render(request, 'create_post.html', context={'form': postfrom})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    postfrom = PostForm(instance=post)
    if request.method == 'POST':
        postfrom = PostForm(request.POST, instance=post) # PostForm-ის შევსება request-ში მოსული მონაცემებით
        if postfrom.is_valid(): # მონაცემების ვალიდურობის შემოწმება
            postfrom.save() # ჩანაწერის ბაზაში შენახვა
            return redirect('home') 
    return render(request, 'update_post.html', context={'form': postfrom})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')
    
