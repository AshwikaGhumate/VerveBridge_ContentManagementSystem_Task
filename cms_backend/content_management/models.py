from django.db import models
from django.utils import timezone
import uuid

class Page(models.Model):
    """
    A generalized model for different types of pages.
    """
    PAGE_TYPE_CHOICES = [
        ('index', 'Index'),
        ('about', 'About'),
        ('booking', 'Booking'),
        ('contact', 'Contact'),
        ('menu', 'Menu'),
        ('service', 'Service'),
        ('team', 'Team'),
        ('testimonial', 'Testimonial'),
    ]

    page_type = models.CharField(max_length=255, choices=PAGE_TYPE_CHOICES, unique=True, default='index')
    title = models.CharField(max_length=255)
    content = models.TextField()  # This can be used to store the content of the page
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True, default='default-slug')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
