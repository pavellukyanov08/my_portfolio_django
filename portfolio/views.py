from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from main_page.models import Menu
from .models import Project


def projects(request):
    menu = Menu.objects.all()
    my_projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'menu': menu, 'projects': my_projects})


def project_details(request, project_id):
    menu = Menu.objects.all()
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project_details.html', {'menu': menu, 'project': project})
