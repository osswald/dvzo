from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View, generic
from django.views.generic import TemplateView


class DvzoMixin(LoginRequiredMixin, PermissionRequiredMixin):
    pass


class DvzoView(DvzoMixin, View):
    pass


class DvzoTemplateView(DvzoMixin, TemplateView):
    pass


class DvzoCreateView(DvzoMixin, generic.CreateView):
    pass


class DvzoListView(DvzoMixin, generic.ListView):
    pass


class DvzoUpdateView(DvzoMixin, generic.UpdateView):
    pass


class DvzoDetailView(DvzoMixin, generic.DetailView):
    pass


class DvzoDeleteView(DvzoMixin, generic.DeleteView):
    pass
