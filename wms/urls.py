"""wms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app import views
urlpatterns = [
    url(r'^user/', views.userView, name='user view'),
    url(r'^admin/', views.adminView, name='admin view'),
    url(r'^service/', views.registerService, name='Service view'),
    url(r'^device/', views.device, name="device"),
    url(r'^test/', views.testAPI, name="test"),
    url(r'^api/', include('app.api.urls', namespace='restapi')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
