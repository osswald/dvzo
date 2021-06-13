from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoUpdateView
from train_management.forms import FunctionForm
from train_management.models import DvzoFunction


class FunctionListView(DvzoListView):
    permission_required = 'train_management.view_dvzofunction'
    context_object_name = "functions"

    def get_queryset(self):
        return DvzoFunction.objects.all()


class FunctionUpdateView(DvzoUpdateView):
    permission_required = 'train_management.change_dvzofunction'
    model = DvzoFunction
    form_class = FunctionForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


class FunctionCreateView(DvzoCreateView):
    permission_required = 'train_management.add_dvzofunction'
    model = DvzoFunction
    form_class = FunctionForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


class FunctionDeleteView(DvzoDeleteView):
    permission_required = 'train_management.delete_dvzofunction'
    model = DvzoFunction
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("function-list")
