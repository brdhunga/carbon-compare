"""ecoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from footprint_app import views as carbon_views
from custom_user import views as user_views

from shipments.views import home as shipments_home


urlpatterns = [
    path('', carbon_views.home, name="index"),
    path('api/footprints', carbon_views.get_footprints),
    path("add", carbon_views.add_carbon_record),
    path('hello', carbon_views.hello),
    # admin
    path('admin/', admin.site.urls),
    # auth login
    path("login", user_views.login, name="login"),
    path("logout", user_views.logout, name="logout"),
    path("callback", user_views.callback, name="callback"),
    path("check", user_views.check_login),
    # 
    path("shipments", shipments_home),
]
