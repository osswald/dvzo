from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from training.forms import TrainingForm
from training.models import Participant, Training, TrainingDate


@method_decorator(login_required, name='dispatch')
class TrainingListView(generic.ListView):
    context_object_name = "trainings"

    def get_queryset(self):
        return Training.objects.all()


@method_decorator(login_required, name='dispatch')
class TrainingDetailView(generic.DetailView):
    model = Training
    form_class = TrainingForm
    template_name_suffix = "_detail_form"

    def get_context_data(self, **kwargs):
        dates = TrainingDate.objects.filter(training=self.object.id).order_by("start_datetime")
        participants = Participant.objects.filter(training=self.object.id).order_by("personnel")
        return super().get_context_data(dates=dates, participants=participants, **kwargs)


@method_decorator(login_required, name='dispatch')
class TrainingUpdateView(generic.UpdateView):
    model = Training
    form_class = TrainingForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("training-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class TrainingCreateView(generic.CreateView):
    model = Training
    form_class = TrainingForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("training-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class TrainingDeleteView(generic.DeleteView):
    model = Training
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("training-list")
