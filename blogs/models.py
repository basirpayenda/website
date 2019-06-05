from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import date
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

def author_document_path(instance, filename):
    today = date.today()
    return f"documents/{ instance.author.username }/{today.year}/{today.month}/{today.day}/{filename}"


def author_blog_images(instance, filename):
    today = date.today()
    return f"blog-images/{instance.author.username}/{today.year}/{today.month}/{today.day}/{filename}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=True, unique=True)
    overview = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to=author_blog_images)
    documents = models.FileField(upload_to=author_document_path, null=True, blank=True)
    featured = models.BooleanField()
    blog_views = models.PositiveIntegerField(default=1)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'blog_slug':self.slug})

    def get_update_url(self):
        return reverse('blog:blog_update', kwargs={'blog_slug':self.slug})
    
    def get_delete_url(self):
        return reverse('blog:blog_delete', kwargs={'blog_slug':self.slug})

    