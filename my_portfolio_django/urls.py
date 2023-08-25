from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # main_page
    path('', views.index, name='index'),
    # about
    path('about/', include('about.urls')),
    # blogs
    path('blogs/', include('blogs.urls')),
    # portfolio
    path('projects/', include('portfolio.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)