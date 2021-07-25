from django.urls import path

from . import views

urlpatterns = [
    path('shifttemplate/', views.ShiftTemplateListView.as_view(), name='shift-template-list'),
    path('shifttemplate/create', views.ShiftTemplateCreateView.as_view(), name='shift-template-create'),
    path('shifttemplate/<int:pk>/update', views.ShiftTemplateUpdateView.as_view(), name='shift-template-update'),
    path('shifftemplate/<int:pk>/delete', views.ShiftTemplateDeleteView.as_view(), name='shift-template-delete'),
]
