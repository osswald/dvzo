from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView
from dvzo.views import DvzoDeleteView
from dvzo.views import DvzoListView
from dvzo.views import DvzoUpdateView
from train_management.forms import StationForm
from train_management.models import Station


class StationListView(DvzoListView):
    permission_required = "train_management.view_station"
    context_object_name = "stations"

    def get_queryset(self):
        return Station.objects.all()


class StationUpdateView(DvzoUpdateView):
    permission_required = "train_management.change_station"
    model = Station
    form_class = StationForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("station-detail", kwargs={"pk": self.object.id})


class StationCreateView(DvzoCreateView):
    permission_required = "train_management.add_station"
    model = Station
    form_class = StationForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("station-detail", kwargs={"pk": self.object.id})


class StationDeleteView(DvzoDeleteView):
    permission_required = "train_management.delete_station"
    model = Station
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("station-list")
