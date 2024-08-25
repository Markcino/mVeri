from django.db import models

# Create your models here.

class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_description = models.TextField()
    about_image = models.ImageField(upload_to='about/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_title

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.CharField(max_length=100)
    blog_body = models.TextField()
    blog_image = models.ImageField(upload_to='blog/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title