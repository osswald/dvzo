from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from training.forms import ParticipantForm
from training.models import Training, Participant


@method_decorator(login_required, name='dispatch')
class ParticipantUpdateView(generic.UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("training-detail", kwargs={'pk': self.object.training.id})


@method_decorator(login_required, name='dispatch')
class ParticipantCreateView(generic.CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name_suffix = "_create_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.training = get_object_or_404(Training, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.training = self.training
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("training-detail", kwargs={'pk': self.object.training.id})


@method_decorator(login_required, name='dispatch')
class ParticipantDeleteView(generic.DeleteView):
    model = Participant

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("training-detail", kwargs={'pk': self.object.training.id})
