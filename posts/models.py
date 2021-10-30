from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user')

    def __str__(self):
        return self.title

class PostImage(models.Model):
    image = models.ImageField(upload_to = 'image',null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_image',null=True, blank=True)

    def __str__(self):
        return self.post.title

