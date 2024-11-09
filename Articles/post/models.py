from django.db import models
from datetime import date

class Post(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateField(default=date.today)
    author = models.CharField(max_length=40)
    like_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    test = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} - {self.author}'

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
