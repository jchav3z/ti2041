"""
URL configuration for creacionapi project.

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
# creacionapi/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import ServiceList, ServiceDetail, ProviderDetail, service_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    path('providers/<int:pk>/', ProviderDetail.as_view(), name='provider-detail'),
    path('services-html/', service_list, name='service-list-html'),
]
