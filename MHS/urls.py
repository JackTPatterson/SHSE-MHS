"""MHS URL Configuration

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
from django.urls import path
from MHS import settings
from users import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('forms', views.forms, name='forms'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('contact-technical', views.contactTechnical, name='contactTechnical'),
    path('contact-general', views.contactGeneral, name='contactGeneral'),
    path('login', views.login, name='login'),
    path('feedback', views.General.as_view(), name='feedback'),
    path('announcements', views.Announcements.as_view(), name='announcements'),
    path('announcement/<int:announcementID>', views.editAnnouncements, name='editAnnouncements'),
    path('dashboard', views.dashboard, name='dashboard'),
]
