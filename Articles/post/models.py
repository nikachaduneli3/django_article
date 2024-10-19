from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateField()
    author = models.CharField(max_length=40)
    like_count = models.IntegerField()
    published = models.BooleanField()
    test = models.IntegerField(default=1)
