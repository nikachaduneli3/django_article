from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):
    postfrom = PostForm()

    if request.method == 'GET':
        postfrom = PostForm(request.GET) # PostForm-ის შევსება request-ში მოსული მონაცემებით
        if postfrom.is_valid(): # მონაცემების ვალიდურობის შემოწმება
            postfrom.save() # ჩანაწერის ბაზაში შენახვა
            return redirect('home') 
    
    
    posts = Post.objects.all() #ყველა პოსტის წამოღება
    context = {'posts': posts,
               'form': postfrom}

    return render(request, 'template_1.html', context=context)  

