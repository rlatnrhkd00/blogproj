"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/home/', blog.views.home, name="home"),
    path('', blog.views.real, name="real"),
    path('blog/<int:blog_id>',blog.views.detail,name="detail"),
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name="create"),  
    path('portfolio', blog.views.port, name="port"),
    path('blog/newblog/', blog.views.blogpost, name="newblog"),
    path('blog/newPort/', blog.views.portpost, name="newPort"),
    path('account/', include('account.urls')),  
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
