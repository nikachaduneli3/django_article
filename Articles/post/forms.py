from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'author', 
                  'create_date', 'like_count',
                  'published', 'test']