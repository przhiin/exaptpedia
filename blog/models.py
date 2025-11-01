from django.db import models
from django.core.exceptions import ValidationError

def validate_file_type(value):
    valid_mime_types = ['image/', 'video/']
    if not any(value.file.content_type.startswith(t) for t in valid_mime_types):
        raise ValidationError('Only image and video files are allowed.')

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    media = models.FileField(
        upload_to='blog_media/',
        validators=[validate_file_type],
        blank=True,
        null=True
    )
    author = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
