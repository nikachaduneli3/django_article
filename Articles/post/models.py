from django.db import models
from datetime import datetime

class Post(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateField(default=datetime.now())
    author = models.CharField(max_length=40)
    like_count = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    test = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} - {self.author}'