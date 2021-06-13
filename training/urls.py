from django.urls import path

from . import views

urlpatterns = [
    # path('', views.CourseListView.as_view(), name='training-home'),

    path('training-module/', views.TrainingModuleListView.as_view(), name='training-module-list'),
    path('training-module/<int:pk>/', views.TrainingModuleUpdateView.as_view(), name='training-module-update'),
    path('training-module/add/', views.TrainingModuleCreateView.as_view(), name='training-module-create'),
    path('training-module/<int:pk>/delete/', views.TrainingModuleDeleteView.as_view(), name='training-module-delete'),

    path('training/', views.TrainingListView.as_view(), name='training-list'),
    path('training/<int:pk>/', views.TrainingDetailView.as_view(), name='training-detail'),
    path('training/<int:pk>/edit/', views.TrainingUpdateView.as_view(), name='training-update'),
    path('training/add/', views.TrainingCreateView.as_view(), name='training-create'),
    path('training/<int:pk>/delete/', views.TrainingDeleteView.as_view(), name='training-delete'),

    path('training/date/<int:pk>/edit/', views.TrainingDateUpdateView.as_view(), name='training-date-update'),
    path('training/<int:pk>/date/add/', views.TrainingDateCreateView.as_view(), name='training-date-create'),
    path('training//date/<int:pk>/delete/', views.TrainingDateDeleteView.as_view(), name='training-date-delete'),

    path('participant/<int:pk>/edit/', views.ParticipantUpdateView.as_view(), name='participant-update'),
    path('<int:pk>/participant/add/', views.ParticipantCreateView.as_view(), name='participant-create'),
    path('participant/<int:pk>/delete/', views.ParticipantDeleteView.as_view(), name='participant-delete'),
]
