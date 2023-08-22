from django.shortcuts import render
from main_page.models import Menu


def blogs(request):
    menu = Menu.objects.all()
    return render(request, 'blogs/blogs.html', {'menu': menu})
