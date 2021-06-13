from datetime import date

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoDetailView, DvzoListView, DvzoUpdateView, DvzoView
from train_management.forms import DayPlanningFieldsetForm
from train_management.models import (CopyRecipient, DayPlanning, DayPlanningText, DvzoFunction, FunctionPersons,
                                     Personnel, Train, TrainTimetable,)


class DayPlanningListView(DvzoListView):
    permission_required = 'train_management.view_dayplanning'
    context_object_name = "day_plannings"

    def get_queryset(self):
        return DayPlanning.objects.all()


class DayPlanningBulletinView(DvzoListView):
    permission_required = 'train_management.view_dayplanning'
    context_object_name = "day_plannings"

    def get_queryset(self):
        today = date.today()
        return DayPlanning.objects.filter(date__gte=today).order_by("date")


class DayPlanningDetailView(DvzoDetailView):
    permission_required = 'train_management.view_dayplanning'
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_detail_form"

    def get_context_data(self, **kwargs):
        function_types = {}
        for functions in _get_dvzo_functions_no_train().filter(functionpersons__dayplanning=self.object):
            function_type = functions.function_type
            function_type_data = {}
            for dvzo_function in DvzoFunction.objects.filter(
                    functionpersons__dayplanning=self.object,
                    function_type=function_type).order_by("sorting"):
                persons = [function_person.person for function_person in FunctionPersons.objects.filter(
                    dayplanning=self.object,
                    dvzo_function=dvzo_function)]
                function_type_data[dvzo_function] = persons
            function_types[function_type] = function_type_data

        trains_data = []
        for train in Train.objects.filter(day_planning=self.object).order_by('pk'):
            functions = {}
            for function in _get_dvzo_functions_train().filter(functionpersons__train=train):
                functions[function] = Personnel.objects.filter(
                    functionpersons__dvzo_function=function,
                    functionpersons__train=train)
            trains_data.append({
                "train": train,
                "functions": functions})

        traintimetables = TrainTimetable.objects.filter(train__in=self.object.train_set.all()).order_by("label")
        dayplanning_texts = DayPlanningText.objects.filter(dayplanning=self.object).order_by("sorting")
        return super().get_context_data(
            dayplanning_functions=function_types,
            trains_data=trains_data,
            traintimetables=traintimetables,
            dayplanning_texts=dayplanning_texts,
            **kwargs)


class DayPlanningUpdateView(DvzoUpdateView):
    permission_required = 'train_management.change_dayplanning'
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


class DayPlanningCreateView(DvzoCreateView):
    permission_required = 'train_management.add_dayplanning'
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


class DayPlanningRecipientView(DvzoDetailView):
    permission_required = 'train_management.view_dayplanning'
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_recipient_form"

    def get_context_data(self, **kwargs):
        copy_recipients = CopyRecipient.objects.all()
        all_active_personnel = _get_personnel()
        working_personnel_train = Personnel.objects.filter(functionpersons__train__in=self.object.train_set.all())
        working_personnel_stationary = Personnel.objects.filter(functionpersons__dayplanning=self.object)
        all_working_personnel = working_personnel_train | working_personnel_stationary
        all_working_personnel_distinct = all_working_personnel.distinct()

        return super().get_context_data(
            copy_recipients=copy_recipients,
            all_active_personnel=all_active_personnel,
            all_working_personnel=all_working_personnel_distinct,
            **kwargs)


class DayPlanningDeleteView(DvzoDeleteView):
    permission_required = 'train_management.delete_dayplanning'
    model = DayPlanning
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("day-planning-list")


class EditTrainFunctions(DvzoView):
    permission_required = 'train_management.change_dayplanning'

    def get(self, request, train_id, **kwargs):
        train = get_object_or_404(Train, pk=train_id)
        dvzo_functions_with_extra_info = []
        for dvzo_function in _get_dvzo_functions_train():
            all_function_persons_of_train = dvzo_function.functionpersons_set.filter(train=train)
            persons_ids = list(set([x.person.id for x in all_function_persons_of_train]))
            dvzo_functions_with_extra_info.append({
                'function': dvzo_function,
                'persons': persons_ids,
            })

        return render(
            self.request, 'train_management/train_functions.html',
            {'functions': dvzo_functions_with_extra_info, 'persons': _get_personnel()})

    def post(self, request, train_id):
        train = get_object_or_404(Train, pk=train_id)
        function_persons = []
        for dvzo_function in _get_dvzo_functions_train():
            persons_in_function_ids = request.POST.getlist(str(dvzo_function.id))
            if persons_in_function_ids:
                for person_id in persons_in_function_ids:
                    function_person = FunctionPersons(
                        person=Personnel.objects.get(pk=person_id),
                        dvzo_function=dvzo_function)
                    function_person.save()
                    function_persons.append(function_person)
        train.function_persons.set(function_persons)
        train.save()
        return redirect("day-planning-detail", pk=train.day_planning.id)


class EditDayPlanningFunctions(DvzoView):
    permission_required = 'train_management.change_dayplanning'

    def get(self, request, dayplanning_id, **kwargs):
        dayplanning = get_object_or_404(DayPlanning, pk=dayplanning_id)
        places = [place for place in DvzoFunction.FunctionType
                  if place != DvzoFunction.FunctionType.TRAIN]
        places.sort(key=lambda x: x.label)
        dvzo_functions_with_extra_info = []
        for dvzo_function in _get_dvzo_functions_no_train():
            all_function_persons_of_dayplanning = dvzo_function.functionpersons_set.filter(dayplanning=dayplanning)
            persons_ids = list(set([x.person.id for x in all_function_persons_of_dayplanning]))
            dvzo_functions_with_extra_info.append({
                'function': dvzo_function,
                'persons': persons_ids,
            })

        return render(
            self.request, 'train_management/dayplanning_functions.html',
            {'places': places,
             'functions': dvzo_functions_with_extra_info,
             'persons': _get_personnel()

             })

    def post(self, request, dayplanning_id):
        dayplanning = get_object_or_404(DayPlanning, pk=dayplanning_id)
        function_persons = []
        for dvzo_function in _get_dvzo_functions_no_train():
            persons_in_function_ids = request.POST.getlist(str(dvzo_function.id))
            if persons_in_function_ids:
                for person_id in persons_in_function_ids:
                    function_person = FunctionPersons(
                        person=Personnel.objects.get(pk=person_id),
                        dvzo_function=dvzo_function)
                    function_person.save()
                    function_persons.append(function_person)
        dayplanning.function_persons.set(function_persons)
        dayplanning.save()
        return redirect("day-planning-detail", pk=dayplanning.id)


def _get_dvzo_functions_train():
    return DvzoFunction.objects.filter(function_type=DvzoFunction.FunctionType.TRAIN).order_by('sorting')


def _get_dvzo_functions_no_train():
    return DvzoFunction.objects.exclude(function_type=DvzoFunction.FunctionType.TRAIN).order_by('sorting')


def _get_personnel():
    return Personnel.objects.filter(status=Personnel.PersonnelStatus.ACTIVE).order_by('user__last_name')
