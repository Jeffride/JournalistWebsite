from django.db import models

# Create your models here.

from django.urls import reverse

class BlogPost(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    blog_title = models.CharField(max_length=50, help_text='Enter Blog Title')
    # …
    blog_content = models.TextField(max_length=50000, help_text='Enter blog post content here')
    # Metadata
    class Meta:
        ordering = ['-blog_title', ]

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the BlogPost object (in Admin site etc.)."""
        return self.blog_title
