from django.shortcuts import render

# Create your views here.


from .models import BlogPost

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = BlogPost.objects.all().count()
 
    context = {
        'num_blogs': num_blogs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
