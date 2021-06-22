from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoUpdateView
from train_management.forms import TrainTimetableTemplateForm
from train_management.models import TrainTimetableTemplate


class TrainTimetableTemplateListView(DvzoListView):
    permission_required = 'train_management.view_traintimetabletemplate'
    context_object_name = "templates"

    def get_queryset(self):
        return TrainTimetableTemplate.objects.all()


class TrainTimetableTemplateUpdateView(DvzoUpdateView):
    permission_required = 'train_management.change_traintimetabletemplate'
    model = TrainTimetableTemplate
    form_class = TrainTimetableTemplateForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("train-timetable-template-detail", kwargs={'pk': self.object.id})


class TrainTimetableTemplateCreateView(DvzoCreateView):
    permission_required = 'train_management.add_traintimetabletemplate'
    model = TrainTimetableTemplate
    form_class = TrainTimetableTemplateForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("train-timetable-template-detail", kwargs={'pk': self.object.id})


class TrainTimetableTemplateDeleteView(DvzoDeleteView):
    permission_required = 'train_management.delete_traintimetabletemplate'
    model = TrainTimetableTemplate
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("train-timetable-template-list")
