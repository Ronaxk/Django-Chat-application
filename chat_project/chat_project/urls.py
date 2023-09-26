"""
URL configuration for chat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView  # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('chatapp.urls')),  # Include chatapp's URLs for register
    path('login/', include('chatapp.urls')),  # Include chatapp's URLs for login
    path('api/', include('chatapp.urls')),  # Include chatapp's API URLs
    path('', TemplateView.as_view(template_name='home.html'), name='home')  # Default view for the root path
    # Add more project-level URLs here
]


