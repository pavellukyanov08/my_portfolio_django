from django.contrib import admin
from django.urls import path, include
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # main_page
    path('', views.index, name='index'),
    # about
    path('about/', include('about.urls')),
    # blogs
    path('blogs/', include('blogs.urls')),
]
