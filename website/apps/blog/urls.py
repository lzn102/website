# !/usr/bin/env python# -*- coding: utf-8 -*-from django.urls import pathfrom . import viewsapp_name = 'blog'urlpatterns = [    path(r'', views.index, name='index'),    path(r'font/', views.font, name='font'),    path(r'back', views.back, name='back'),    path(r'tools', views.tools, name='tools'),    path(r'content/<int:title_id>/', views.content, name='content'),]