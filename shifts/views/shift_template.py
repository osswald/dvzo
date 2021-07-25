from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoUpdateView
from shifts.forms import ShiftTemplateForm
from shifts.models import ShiftTemplate


class ShiftTemplateListView(DvzoListView):
    permission_required = 'shifts.view_shifttemplate'
    context_object_name = "shift_templates"

    def get_queryset(self):
        return ShiftTemplate.objects.all()


class ShiftTemplateUpdateView(DvzoUpdateView):
    permission_required = 'shifts.change_shifttemplate'
    model = ShiftTemplate
    form_class = ShiftTemplateForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("shift-template-update", kwargs={'pk': self.object.id})


class ShiftTemplateCreateView(DvzoCreateView):
    permission_required = 'shifts.add_shifttemplate'
    model = ShiftTemplate
    form_class = ShiftTemplateForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("shift-template-update", kwargs={'pk': self.object.id})


class ShiftTemplateDeleteView(DvzoDeleteView):
    permission_required = 'shifts.delete_shifttemplate'
    model = ShiftTemplate
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("shift-template-list")
