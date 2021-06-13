from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from training.forms import TrainingModuleForm
from training.models import TrainingModule


@method_decorator(login_required, name='dispatch')
class TrainingModuleListView(generic.ListView):
    context_object_name = "training_modules"

    def get_queryset(self):
        return TrainingModule.objects.all()


@method_decorator(login_required, name='dispatch')
class TrainingModuleUpdateView(generic.UpdateView):
    model = TrainingModule
    form_class = TrainingModuleForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("training-module-list")


@method_decorator(login_required, name='dispatch')
class TrainingModuleCreateView(generic.CreateView):
    model = TrainingModule
    form_class = TrainingModuleForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("training-module-list")


@method_decorator(login_required, name='dispatch')
class TrainingModuleDeleteView(generic.DeleteView):
    model = TrainingModule
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("training-module-list")
