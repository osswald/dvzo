from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView
from dvzo.views import DvzoDeleteView
from dvzo.views import DvzoListView
from dvzo.views import DvzoUpdateView
from dvzo.views import DvzoView
from train_management.forms import TrainTimetableTemplateForm
from train_management.models import Train
from train_management.models import TrainTimetableTemplate


class TrainTimetableTemplateListView(DvzoListView):
    permission_required = "train_management.view_traintimetabletemplate"
    context_object_name = "templates"

    def get_queryset(self):
        return TrainTimetableTemplate.objects.all()


class TrainTimetableTemplateUpdateView(DvzoUpdateView):
    permission_required = "train_management.change_traintimetabletemplate"
    model = TrainTimetableTemplate
    form_class = TrainTimetableTemplateForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("train-timetable-template-detail", kwargs={"pk": self.object.id})


class TrainTimetableTemplateCreateView(DvzoCreateView):
    permission_required = "train_management.add_traintimetabletemplate"
    model = TrainTimetableTemplate
    form_class = TrainTimetableTemplateForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("train-timetable-template-detail", kwargs={"pk": self.object.id})


class TrainTimetableTemplateDeleteView(DvzoDeleteView):
    permission_required = "train_management.delete_traintimetabletemplate"
    model = TrainTimetableTemplate
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("train-timetable-template-list")


class CreateTimetablesFromTemplateView(DvzoView):
    permission_required = "train_management_add_traintimetable"

    def post(self, request, **kwargs):
        timetable_ids = request.POST["timetables"].split(",")
        train_id = request.POST["pk"]
        timetables = [get_object_or_404(TrainTimetableTemplate, pk=pk) for pk in timetable_ids]
        train = get_object_or_404(Train, pk=train_id)
        train.add_traintimetables(timetables)
        return redirect("day-planning-detail", pk=train.day_planning.id)


class ChooseTimetableTemplatesView(DvzoListView):
    permission_required = "train_management.view_traintimetabletemplate"
    context_object_name = "templates"
    template_name = "train_management/traintimetabletemplate_list.html"

    def get_queryset(self):
        return TrainTimetableTemplate.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ChooseTimetableTemplatesView, self).get_context_data(**kwargs)
        context["train"] = self.request.GET["train"]
        return context
