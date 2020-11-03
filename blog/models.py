from django.contrib.auth.models import User
from djongo import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    is_liked = models.BooleanField(default=False)
    total = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "_" + self.author.username

    def total_likes(self):
        return self.likes.count()

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title + "Image"