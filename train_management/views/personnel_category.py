from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import PersonnelCategoryForm
from train_management.models import PersonnelCategory


@method_decorator(login_required, name='dispatch')
class PersonnelCategoryListView(generic.ListView):
    context_object_name = "personnel_categories"

    def get_queryset(self):
        return PersonnelCategory.objects.all()


@method_decorator(login_required, name='dispatch')
class PersonnelCategoryUpdateView(generic.UpdateView):
    model = PersonnelCategory
    form_class = PersonnelCategoryForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("personnel-category-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PersonnelCategoryCreateView(generic.CreateView):
    model = PersonnelCategory
    form_class = PersonnelCategoryForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("personnel-category-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PersonnelCategoryDeleteView(generic.DeleteView):
    model = PersonnelCategory
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("personnel-category-list")
