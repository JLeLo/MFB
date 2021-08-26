"""mfb_root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView
from mfb import views

# from mfb.views import index

urlpatterns = [
    path('', views.index, name='index'),
    # API1
    path('admin', admin.site.urls),
    path(r'^static/(?P<path>.*)$', serve,
         {"document_root": settings.STATIC_ROOT}),
    path('api-auth/', include('rest_framework.urls')),
    path('checks/<int:pk>', views.fetch_checks),
    path('all_checks/', views.all_checks),
    path('all_projects/', views.all_projects),

]
