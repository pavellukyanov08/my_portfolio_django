from django.shortcuts import render, get_object_or_404
from main_page.models import Menu
from .models import Blog


def blogs(request):
    menu = Menu.objects.all()
    blogi = Blog.objects.all().order_by('-date')
    return render(request, 'blogs/blogs.html', {'menu': menu, 'blogs': blogi})


def blog_details(request, blog_id):
    menu = Menu.objects.all()
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/blog_details.html', {'menu': menu, 'blog': blog})
