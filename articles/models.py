from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)#Keeps articles even if the user is deleted




    def save(self, *args, **kwargs):
        if not self.slug and self.title:  # Auto-generate slug only if it's empty
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'......'
      

