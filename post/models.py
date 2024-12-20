from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    comments=models.ManyToManyField(Post)
    name=models.CharField(max_length=150)
    your_comment=models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name} {self.your_comment}'


