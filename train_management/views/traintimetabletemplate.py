from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import TrainTimetableTemplateForm
from train_management.models import TrainTimetableTemplate


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
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("train-timetable-template-list")
