from django.db import models
import json
from django.core.exceptions import ObjectDoesNotExist

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Non-Binary', 'Non-Binary'),
]

OCCUPATION_CHOICES = [
    ('Manager', 'Manager'),
    ('Social Worker', 'Social Worker'),
    ('Doctor', 'Doctor'),
    ('Entrepreneur', 'Entrepreneur'),
    ('Other', 'Other - Specify'),
]


class JobCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job Category"
        verbose_name_plural = "Job Categories"
        ordering = ['name']


class Members(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, default='',)
    email = models.EmailField(unique=True,blank = True, null = True)


    occupation_category = models.ForeignKey(
        JobCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="occupation_category",
        verbose_name="Occupation Category"
    )
    position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Postion and Organization/Company"
    )

    profile_image = models.ImageField(
        upload_to='user_images/',
        null=True,
        blank=True,
        default='user_images/default.png'
    )

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"


# ✅ Optional helper: Load Job Categories from JSON
    def load_job_categories_from_json(json_path):
        with open(json_path, 'r') as f:
            data = json.load(f)
        for category in data.get("categories", []):
            JobCategory.objects.get_or_create(name=category)

    