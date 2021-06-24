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
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('frequency-chart/', views.FrequencyChartData.as_view(), name='frequency-chart'),

    path('calendar/', views.Calendar.as_view(), name='calendar'),
    path('calendar/event_data', views.CalendarAvailabilityData.as_view(), name='event-data'),
    path('calendar/resource_data', views.CalendarResourceData.as_view(), name='resource-data'),

    path('dayplanning/', views.DayPlanningListView.as_view(), name='day-planning-list'),
    path('dayplanning/detail/<int:pk>/', views.DayPlanningDetailView.as_view(), name='day-planning-detail'),
    path('dayplanning/detail/<int:pk>/recipients', views.DayPlanningRecipientView.as_view(),
         name='day-planning-recipients'),
    path('dayplanning/update/<int:pk>/', views.DayPlanningUpdateView.as_view(), name='day-planning-update'),
    path('dayplanning/add/', views.DayPlanningCreateView.as_view(), name='day-planning-create'),
    path('dayplanning/<int:pk>/delete/', views.DayPlanningDeleteView.as_view(), name='day-planning-delete'),

    path('dayplanning/text/add/<int:pk>/', views.DayPlanningTextCreateView.as_view(), name='day-planning-text-create'),
    path('dayplanning/text/<int:pk>/', views.DayPlanningTextUpdateView.as_view(), name='day-planning-text-update'),
    path('dayplanning/text/delete/<int:pk>/',
         views.DayPlanningTextDeleteView.as_view(), name='day-planning-text-delete'),

    path('dayplanning/<int:pk>/briefing/', views.BriefingPrintView.as_view(template_name="pdf/briefing.html"),
         name='briefing-pdf'),
    path('bulletin/', views.BulletinPrintView.as_view(template_name="pdf/bulletin.html"),
         name='bulletin-pdf'),

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
    path('carriage/<int:pk>/', views.CarriageDetailView.as_view(), name='carriage-detail'),
    path('carriage/<int:pk>/update/', views.CarriageUpdateView.as_view(), name='carriage-update'),
    path('carriage/add/', views.CarriageCreateView.as_view(), name='carriage-create'),
    path('carriage/<int:pk>/delete/', views.CarriageDeleteView.as_view(), name='carriage-delete'),

    path('engine/', views.EngineListView.as_view(), name='engine-list'),
    path('engine/<int:pk>/', views.EngineDetailView.as_view(), name='engine-detail'),
    path('engine/<int:pk>/update', views.EngineUpdateView.as_view(), name='engine-update'),
    path('engine/add/', views.EngineCreateView.as_view(), name='engine-create'),
    path('engine/<int:pk>/delete/', views.EngineDeleteView.as_view(), name='engine-delete'),

    path('phone/', views.PhoneNumberListView.as_view(), name='phone-list'),
    path('phone/<int:pk>/', views.PhoneNumberUpdateView.as_view(), name='phone-detail'),
    path('phone/add/', views.PhoneNumberCreateView.as_view(), name='phone-create'),
    path('phone/<int:pk>/delete/', views.PhoneNumberDeleteView.as_view(), name='phone-delete'),

    path('phonenumber/', views.PhoneNumberOverview.as_view(), name='phonenumber-list'),
    path('phonenumber/member/', views.PhoneNumberMemberList.as_view(), name='phonenumber-member-detail'),
    path('phonenumber/type/', views.PhoneNumberDetail.as_view(), name='phonenumber-detail'),

    path('station/', views.StationListView.as_view(), name='station-list'),
    path('station/<int:pk>/', views.StationUpdateView.as_view(), name='station-detail'),
    path('station/add/', views.StationCreateView.as_view(), name='station-create'),
    path('station/<int:pk>/delete/', views.StationDeleteView.as_view(), name='station-delete'),

    path('dayplanning/train/reservation/add/<int:pk>/',
         views.ReservationCreateView.as_view(), name='reservation-create'),
    path('dayplanning/train/reservation/<int:pk>/',
         views.ReservationUpdateView.as_view(), name='reservation-update'),
    path('dayplanning/train/reservation/',
         views.ReservationListView.as_view(), name='reservation-list'),
    path('dayplanning/train/reservation/delete/<int:pk>/',
         views.ReservationDeleteView.as_view(), name='reservation-delete'),

    path('dayplanning/train/timetable/add/<int:pk>/',
         views.TrainTimetableCreateView.as_view(), name='train-timetable-create'),
    path('dayplanning/train/timetable/<int:pk>/',
         views.TrainTimetableUpdateView.as_view(), name='train-timetable-update'),
    path('dayplanning/train/timetable/delete/<int:pk>/',
         views.TrainTimetableUpdateView.as_view(), name='train-timetable-delete'),

    path('traintimetabletemplate/',
         views.TrainTimetableTemplateListView.as_view(), name='train-timetable-template-list'),
    path('traintimetabletemplate/choose/',
         views.ChooseTimetableTemplatesView.as_view(), name='train-timetable-template-choose'),
    path('traintimetabletemplate/use/',
         views.CreateTimetablesFromTemplateView.as_view(), name='train-timetable-template-use'),
    path('traintimetabletemplate/<int:pk>/',
         views.TrainTimetableTemplateUpdateView.as_view(), name='train-timetable-template-detail'),
    path('traintimetabletemplate/add/',
         views.TrainTimetableTemplateCreateView.as_view(), name='train-timetable-template-create'),
    path('traintimetabletemplate/<int:pk>/delete/',
         views.TrainTimetableTemplateDeleteView.as_view(), name='train-timetable-template-delete'),

    path('edit-train-functions/<int:train_id>',
         views.EditTrainFunctions.as_view(), name='edit-train-functions'),
    path('edit-dayplanning-functions/<int:dayplanning_id>',
         views.EditDayPlanningFunctions.as_view(), name='edit-dayplanning-functions'),
    path('traincomposition/add/<int:pk>/', views.TrainCompositionCreateView.as_view(), name='train-composition-create'),

    path('availability/', views.AvailabilityListView.as_view(), name='availability-list'),
    path('availability/engine/<int:pk>/',
         views.AvailabilityEngineUpdateView.as_view(), name='availability-engine-detail'),
    path('availability/carriage/<int:pk>/',
         views.AvailabilityCarriageUpdateView.as_view(), name='availability-carriage-detail'),
    path('availability/engine/add/<int:pk>',
         views.AvailabilityEngineCreateView.as_view(), name='availability-engine-create'),
    path('availability/carriage/add/<int:pk>',
         views.AvailabilityCarriageCreateView.as_view(), name='availability-carriage-create'),
    path('availability/<int:pk>/delete/', views.AvailabilityDeleteView.as_view(), name='availability-delete'),

    path('reservation-calendar/', views.ReservationCalendar.as_view(), name='reservation-calendar'),
    path('reservation-calendar/<int:pk>', views.ReservationCalendarTrains.as_view(),
         name='reservation-calendar-trains'),

    path('copy-recipient/', views.CopyRecipientListView.as_view(), name='copy-recipient-list'),
    path('copy-recipient/table',
         views.CopyRecipientListView.as_view(template_name="train_management/copyrecipient_table.html"),
         name='copy-recipient-table'),
    path('copy-recipient/<int:pk>/', views.CopyRecipientUpdateView.as_view(), name='copy-recipient-detail'),
    path('copy-recipient/add/', views.CopyRecipientCreateView.as_view(), name='copy-recipient-create'),
    path('copy-recipient/<int:pk>/delete/', views.CopyRecipientDeleteView.as_view(), name='copy-recipient-delete'),

    path('personnel-category/', views.PersonnelCategoryListView.as_view(), name='personnel-category-list'),
    path('personnel-category/<int:pk>/', views.PersonnelCategoryUpdateView.as_view(), name='personnel-category-detail'),
    path('personnel-category/add/', views.PersonnelCategoryCreateView.as_view(), name='personnel-category-create'),
    path('personnel-category/<int:pk>/delete/', views.PersonnelCategoryDeleteView.as_view(),
         name='personnel-category-delete'),
]
