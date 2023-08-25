from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.project_details, name='project_details'),
]