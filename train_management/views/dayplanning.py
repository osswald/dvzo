from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import DayPlanningFieldsetForm
from train_management.models import DayPlanning, DvzoFunction, FunctionPersons, Personnel, Train


@method_decorator(login_required, name='dispatch')
class DayPlanningListView(generic.ListView):
    context_object_name = "day_plannings"

    def get_queryset(self):
        return DayPlanning.objects.all()


@method_decorator(login_required, name='dispatch')
class DayPlanningDetailView(generic.DetailView):
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_detail_form"


@method_decorator(login_required, name='dispatch')
class DayPlanningUpdateView(generic.UpdateView):
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningCreateView(generic.CreateView):
    model = DayPlanning
    form_class = DayPlanningFieldsetForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningDeleteView(generic.DeleteView):
    model = DayPlanning
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("day-planning-list")


@method_decorator(login_required, name='dispatch')
class EditTrainFunctions(generic.View):
    dvzo_functions = DvzoFunction.objects.filter(function_type=DvzoFunction.FunctionType.TRAIN).order_by('sorting')
    persons = Personnel.objects.filter(status=Personnel.PersonnelStatus.ACTIVE).order_by('user__last_name')

    def get(self, request, train_id, **kwargs):
        train = get_object_or_404(Train, pk=train_id)
        dvzo_functions_with_extra_info = []
        for dvzo_function in self.dvzo_functions:
            all_function_persons_of_train = dvzo_function.functionpersons_set.filter(train=train)
            persons_ids = list(set([x.person.id for x in all_function_persons_of_train]))
            dvzo_functions_with_extra_info.append({
                'function': dvzo_function,
                'persons': persons_ids,
            })

        return render(
            self.request, 'train_management/train_functions.html',
            {'functions': dvzo_functions_with_extra_info, 'persons': self.persons})

    def post(self, request, train_id):
        train = get_object_or_404(Train, pk=train_id)
        function_persons = []
        for dvzo_function in self.dvzo_functions:
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


@method_decorator(login_required, name='dispatch')
class EditDayPlanningFunctions(generic.View):
    dvzo_functions = DvzoFunction.objects.exclude(function_type=DvzoFunction.FunctionType.TRAIN).order_by('sorting')
    persons = Personnel.objects.filter(status=Personnel.PersonnelStatus.ACTIVE).order_by('user__last_name')

    def get(self, request, dayplanning_id, **kwargs):
        dayplanning = get_object_or_404(DayPlanning, pk=dayplanning_id)
        places = [place for place in DvzoFunction.FunctionType
                  if place != DvzoFunction.FunctionType.TRAIN]
        places.sort(key=lambda x: x.label)
        dvzo_functions_with_extra_info = []
        for dvzo_function in self.dvzo_functions:
            all_function_persons_of_dayplanning = dvzo_function.functionpersons_set.filter(dayplanning=dayplanning)
            persons_ids = list(set([x.person.id for x in all_function_persons_of_dayplanning]))
            dvzo_functions_with_extra_info.append({
                'function': dvzo_function,
                'persons': persons_ids,
            })

        return render(
            self.request, 'train_management/dayplanning_functions.html',
            {'places': places, 'functions': dvzo_functions_with_extra_info, 'persons': self.persons})

    def post(self, request, dayplanning_id):
        dayplanning = get_object_or_404(DayPlanning, pk=dayplanning_id)
        function_persons = []
        for dvzo_function in self.dvzo_functions:
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
