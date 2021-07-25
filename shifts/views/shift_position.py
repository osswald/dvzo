from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoUpdateView
from shifts.forms import ShiftPositionForm
from shifts.models import ShiftPosition


class ShiftPositionListView(DvzoListView):
    permission_required = 'shifts.view_shiftposition'
    context_object_name = "shift_templates"

    def get_queryset(self):
        return ShiftPosition.objects.all()


class ShiftPositionUpdateView(DvzoUpdateView):
    permission_required = 'shifts.change_shiftposition'
    model = ShiftPosition
    form_class = ShiftPositionForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("shift-position-update", kwargs={'pk': self.object.id})


class ShiftPositionCreateView(DvzoCreateView):
    permission_required = 'shifts.add_shiftposition'
    model = ShiftPosition
    form_class = ShiftPositionForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("shift-position-update", kwargs={'pk': self.object.id})


class ShiftPositionDeleteView(DvzoDeleteView):
    permission_required = 'shifts.delete_shiftposition'
    model = ShiftPosition
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("shift-position-list")
