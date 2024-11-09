from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm): 
    """ ფორმა Post მოდელისთვის """
    class Meta:
        model = Post
        fields = ['name', 'content', 'author', 
                  'create_date', 'like_count',
                  'published', 'test']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']