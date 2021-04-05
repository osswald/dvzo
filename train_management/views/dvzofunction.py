from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import FunctionForm
from train_management.models import DvzoFunction


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
