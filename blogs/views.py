from django.shortcuts import render
from main_page.models import Menu
from .models import Blog


def blogs(request):
    menu = Menu.objects.all()
    blogi = Blog.objects.all()
    return render(request, 'blogs/blogs.html', {'menu': menu, 'blogs': blogi})
