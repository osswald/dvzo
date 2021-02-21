"""dvzo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dayplanning/', views.DayPlanningListView.as_view(), name='day-planning-list'),
    path('dayplanning/<int:pk>/', views.DayPlanningUpdateView.as_view(), name='day-planning-detail'),
    path('dayplanning/add/', views.DayPlanningCreateView.as_view(), name='day-planning-create'),
    path('dayplanning/<int:pk>/delete/', views.DayPlanningDeleteView.as_view(), name='day-planning-delete'),

    path('personnel/', views.PersonnelListView.as_view(), name='personnel-list'),
    path('personnel/<int:pk>/', views.PersonnelUpdateView.as_view(), name='personnel-detail'),
    path('personnel/add/', views.PersonnelCreateView.as_view(), name='personnel-create'),
    path('personnel/<int:pk>/delete/', views.PersonnelDeleteView.as_view(), name='personnel-delete'),
]
