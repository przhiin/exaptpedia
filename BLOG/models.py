from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    banner = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title