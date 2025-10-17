from django.db import models

# Create your models here.
from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text="Optional external link or proof")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
