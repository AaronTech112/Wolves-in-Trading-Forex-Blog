from email.policy import default
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(unique=True, null=True)
    profile = models.ImageField(null=True, upload_to=' ' ,default='avatar.svg')
    
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = []

class Category(models.Model):
    name = models.CharField(max_length = 200)
    cat_image = models.ImageField(null=True, default='bg1.png')

    def __str__(self):
        return self.name     
    
class Post(models.Model):
    title = models.CharField(max_length=1000)
    subtitle= models.CharField(null=True,max_length=1000)
    image = models.ImageField(null=True,upload_to=' ' ,default='bg1.png')
    body = models.TextField(null=True)
    Links = models.TextField(null=True)
    LinkTitle = models.CharField(null=True,max_length=1000)
    FinalQuote = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    avatar = models.ImageField(null=True, default='avatar.svg')
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    text = models.TextField(max_length=200,null=True)
    post= models.ForeignKey(Post, on_delete=models.CASCADE, null = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



