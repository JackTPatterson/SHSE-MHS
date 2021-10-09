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
from django.shortcuts import render
from django.urls import path
from MHS import settings
from users import views
from django.template import RequestContext

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
    path('announcements/new', views.addAnnouncements, name='newAnnouncements'),

    path('announcement/<int:announcementID>', views.editAnnouncements, name='editAnnouncements'),
    path('announcement/<int:announcementID>/delete', views.deleteAnnouncements.as_view(), name='deleteAnnouncements'),

    path('dates', views.DatesList.as_view(), name='dates'),
    path('date/new', views.addDates, name='newDate'),
    path('date/<int:pk>', views.editDates, name='editDates'),
    path('date/<int:pk>/delete', views.deleteDates.as_view(), name='deleteDate'),

    path('inductees', views.InducteesList.as_view(), name='inductees'),
    path('inductees/new', views.addInductees, name='newInductees'),
    path('inductees/<int:pk>', views.editInductees, name='editInductees'),
    path('logout', views.logout_view, name='logout-view')


]

handler404 = "users.views.page_not_found_view"
