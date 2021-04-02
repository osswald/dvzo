from django.shortcuts import redirect
from django.shortcuts import render
from django_tex.shortcuts import render_to_pdf
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from train_management.models import FunctionPersons

from train_management.models import DayPlanning
from train_management.models import Personnel
from train_management.models import DvzoFunction
from train_management.models import Train
from train_management.models import Vehicle
from train_management.models import Station
from train_management.models import TrainTimetable
from train_management.models import TrainTimetableTemplate
from train_management.forms import DayPlanningForm
from train_management.forms import PersonnelForm
from train_management.forms import FunctionForm
from train_management.forms import TrainForm
from train_management.forms import CarriageForm
from train_management.forms import EngineForm
from train_management.forms import StationForm
from train_management.forms import TrainTimetableForm
from train_management.forms import TrainTimetableTemplateForm


@login_required
def dashboard(request):
    return render(request, "train_management/dashboard.html")


@method_decorator(login_required, name='dispatch')
class DayPlanningListView(generic.ListView):
    context_object_name = "day_plannings"

    def get_queryset(self):
        return DayPlanning.objects.all()


@method_decorator(login_required, name='dispatch')
class DayPlanningDetailView(generic.DetailView):
    model = DayPlanning
    form_class = DayPlanningForm
    template_name_suffix = "_detail_form"


@method_decorator(login_required, name='dispatch')
class DayPlanningUpdateView(generic.UpdateView):
    model = DayPlanning
    form_class = DayPlanningForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningCreateView(generic.CreateView):
    model = DayPlanning
    form_class = DayPlanningForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningDeleteView(generic.DeleteView):
    model = DayPlanning
    success_url = reverse_lazy("day-planning-list")


@method_decorator(login_required, name='dispatch')
class PersonnelListView(generic.ListView):
    context_object_name = "personnels"

    def get_queryset(self):
        return Personnel.objects.all()


@method_decorator(login_required, name='dispatch')
class PersonnelUpdateView(generic.UpdateView):
    model = Personnel
    form_class = PersonnelForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("personnel-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PersonnelCreateView(generic.CreateView):
    model = Personnel
    form_class = PersonnelForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("personnel-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PersonnelDeleteView(generic.DeleteView):
    model = Personnel
    success_url = reverse_lazy("personnel-list")


@method_decorator(login_required, name='dispatch')
class FunctionListView(generic.ListView):
    context_object_name = "functions"

    def get_queryset(self):
        return DvzoFunction.objects.all()


@method_decorator(login_required, name='dispatch')
class FunctionUpdateView(generic.UpdateView):
    model = DvzoFunction
    form_class = FunctionForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class FunctionCreateView(generic.CreateView):
    model = DvzoFunction
    form_class = FunctionForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class FunctionDeleteView(generic.DeleteView):
    model = DvzoFunction
    success_url = reverse_lazy("function-list")


@method_decorator(login_required, name='dispatch')
class TrainCompositionUpdateView(generic.UpdateView):
    model = Train
    form_class = TrainForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_vehicles"] = Vehicle.objects.all().exclude(trainconfiguration__train=self.object)
        return context

    def post(self, request, pk, **kwargs):
        vehicle_ids = request.POST["ordering"].split(",")
        vehicles = [get_object_or_404(Vehicle, pk=pk) for pk in vehicle_ids]
        train = get_object_or_404(Train, pk=pk)
        train.set_composition(vehicles)
        return super().post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.day_planning.id})


@method_decorator(login_required, name='dispatch')
class TrainCompositionCreateView(generic.CreateView):
    model = Train
    form_class = TrainForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_vehicles"] = Vehicle.objects.all()
        return context

    def post(self, request, pk, **kwargs):
        vehicle_ids = request.POST["ordering"].split(",")
        self.vehicles = [get_object_or_404(Vehicle, pk=pk) for pk in vehicle_ids]
        self.day_planning = get_object_or_404(DayPlanning, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.day_planning = self.day_planning
        return_value = super().form_valid(form)
        self.object.set_composition(self.vehicles)
        return return_value

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.day_planning.id})


@method_decorator(login_required, name='dispatch')
class CarriageListView(generic.ListView):
    context_object_name = "carriages"
    queryset = Vehicle.objects.filter(vehicle_type="carriage")
    template_name = "train_management/carriage_list.html"


@method_decorator(login_required, name='dispatch')
class CarriageUpdateView(generic.UpdateView):
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_update_form.html"

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class CarriageCreateView(generic.CreateView):
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_create_form.html"

    def form_valid(self, form):
        form.instance.vehicle_type = "carriage"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class CarriageDeleteView(generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("carriage-list")


@method_decorator(login_required, name='dispatch')
class EngineListView(generic.ListView):
    context_object_name = "engines"
    queryset = Vehicle.objects.filter(vehicle_type="engine")
    template_name = "train_management/engine_list.html"


@method_decorator(login_required, name='dispatch')
class EngineUpdateView(generic.UpdateView):
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_update_form.html"

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class EngineCreateView(generic.CreateView):
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_create_form.html"

    def form_valid(self, form):
        form.instance.vehicle_type = "engine"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class EngineDeleteView(generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("engine-list")

 
@login_required
def briefing_pdf(request, pk):
    template_name = 'latex/briefing.tex'
    dayplanning = DayPlanning.objects.get(pk=pk)
    context = {'dayplanning': dayplanning}
    return render_to_pdf(request, template_name, context, filename='briefing.pdf')


@method_decorator(login_required, name='dispatch')
class StationListView(generic.ListView):
    context_object_name = "stations"

    def get_queryset(self):
        return Station.objects.all()


@method_decorator(login_required, name='dispatch')
class StationUpdateView(generic.UpdateView):
    model = Station
    form_class = StationForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("station-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class StationCreateView(generic.CreateView):
    model = Station
    form_class = StationForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("station-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class StationDeleteView(generic.DeleteView):
    model = Station
    success_url = reverse_lazy("station-list")


@method_decorator(login_required, name='dispatch')
class TrainTimetableCreateView(generic.CreateView):
    model = TrainTimetable
    form_class = TrainTimetableForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.train = get_object_or_404(Train, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.train = self.train
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train.day_planning.id})


@method_decorator(login_required, name='dispatch')
class TrainTimetableUpdateView(generic.UpdateView):
    model = TrainTimetable
    form_class = TrainTimetableForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train.day_planning.id})


@method_decorator(login_required, name='dispatch')
class TrainTimetableDeleteView(generic.DeleteView):
    model = TrainTimetable
    success_url = reverse_lazy("day-planning-list")


@method_decorator(login_required, name='dispatch')
class TrainTimetableTemplateListView(generic.ListView):
    context_object_name = "templates"

    def get_queryset(self):
        return TrainTimetableTemplate.objects.all()


@method_decorator(login_required, name='dispatch')
class TrainTimetableTemplateUpdateView(generic.UpdateView):
    model = TrainTimetableTemplate
    form_class = TrainTimetableTemplateForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("train-timetable-template-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class TrainTimetableTemplateCreateView(generic.CreateView):
    model = TrainTimetableTemplate
    form_class = TrainTimetableTemplateForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("train-timetable-template-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class TrainTimetableTemplateDeleteView(generic.DeleteView):
    model = TrainTimetableTemplate
    success_url = reverse_lazy("train-timetable-template-list")


@method_decorator(login_required, name='dispatch')
class EditTrainFunctions(generic.View):
    dvzo_functions = DvzoFunction.objects.filter(function_type=DvzoFunction.FunctionType.TRAIN).order_by('sorting')
    persons = Personnel.objects.filter(status=Personnel.PersonnelStatus.ACTIVE).order_by('lastname')

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
    persons = Personnel.objects.filter(status=Personnel.PersonnelStatus.ACTIVE).order_by('lastname')

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
