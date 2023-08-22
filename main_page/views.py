from django.shortcuts import render
from .models import Menu


def index(request):
    menu = Menu.objects.all()
    return render(request, 'main_page/index.html', {'menu': menu})
