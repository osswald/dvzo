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
    path('dayplanning/detail/<int:pk>/', views.DayPlanningDetailView.as_view(), name='day-planning-detail'),
    path('dayplanning/update/<int:pk>/', views.DayPlanningUpdateView.as_view(), name='day-planning-update'),
    path('dayplanning/add/', views.DayPlanningCreateView.as_view(), name='day-planning-create'),
    path('dayplanning/<int:pk>/delete/', views.DayPlanningDeleteView.as_view(), name='day-planning-delete'),

    path('dayplanning/<int:pk>/briefing/', views.briefing_pdf, name='briefing-pdf'),

    path('personnel/', views.PersonnelListView.as_view(), name='personnel-list'),
    path('personnel/<int:pk>/', views.PersonnelUpdateView.as_view(), name='personnel-detail'),
    path('personnel/add/', views.PersonnelCreateView.as_view(), name='personnel-create'),
    path('personnel/<int:pk>/delete/', views.PersonnelDeleteView.as_view(), name='personnel-delete'),

    path('function/', views.FunctionListView.as_view(), name='function-list'),
    path('function/<int:pk>/', views.FunctionUpdateView.as_view(), name='function-detail'),
    path('function/add/', views.FunctionCreateView.as_view(), name='function-create'),
    path('function/<int:pk>/delete/', views.FunctionDeleteView.as_view(), name='function-delete'),

    path('traincomposition/<int:pk>/', views.TrainCompositionUpdateView.as_view(), name='train-composition-update'),
    path('traincomposition/add/<int:pk>/', views.TrainCompositionCreateView.as_view(), name='train-composition-create'),

    path('carriage/', views.CarriageListView.as_view(), name='carriage-list'),
    path('carriage/<int:pk>/', views.CarriageUpdateView.as_view(), name='carriage-detail'),
    path('carriage/add/', views.CarriageCreateView.as_view(), name='carriage-create'),
    path('carriage/<int:pk>/delete/', views.CarriageDeleteView.as_view(), name='carriage-delete'),

    path('engine/', views.EngineListView.as_view(), name='engine-list'),
    path('engine/<int:pk>/', views.EngineUpdateView.as_view(), name='engine-detail'),
    path('engine/add/', views.EngineCreateView.as_view(), name='engine-create'),
    path('engine/<int:pk>/delete/', views.EngineDeleteView.as_view(), name='engine-delete'),
]
