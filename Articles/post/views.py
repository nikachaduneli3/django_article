from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm


def home(request):

    posts = Post.objects.all() #ყველა პოსტის წამოღება

    return render(request, 'template_1.html', context={'posts': posts})  


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk) # pk(id) -ით ბაზიდან პოსტის წამოღება

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail-post', pk=pk)
    return render(request, 'detail_post.html', context={'post': post, 'form': CommentForm()})


def create_post(request):
    if request.method == 'POST':
        postfrom = PostForm(request.POST) # PostForm-ის შევსება request-ში მოსული მონაცემებით
        if postfrom.is_valid(): # მონაცემების ვალიდურობის შემოწმება
            postfrom.save() # ჩანაწერის ბაზაში შენახვა
            return redirect('home') 
    return render(request, 'create_post.html', context={'form': PostForm()})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        postfrom = PostForm(request.POST, instance=post) # PostForm-ს თუ instance-ად გადაცემ შენ ობიექს ახლის შექმნი მაგოვრად იმ შენს გადაცემულ ობიუექტს განაახლებს
        if postfrom.is_valid(): # მონაცემების ვალიდურობის შემოწმება
            postfrom.save() # ჩანაწერის ბაზაში შენახვა
            return redirect('home') 
    return render(request, 'update_post.html', 
                  context={'form': PostForm(instance=post)}) # PostForm-ს instance-ად გადააწოდე შენი პოსტი და ფორმაში ველები უკვე შევსებული იქნება მონაცემებით


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')
    
