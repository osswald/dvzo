from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView
from dvzo.views import DvzoDeleteView
from dvzo.views import DvzoListView
from dvzo.views import DvzoUpdateView
from train_management.forms import PersonnelCategoryForm
from train_management.models import PersonnelCategory


class PersonnelCategoryListView(DvzoListView):
    permission_required = "train_management.view_personnelcategory"
    context_object_name = "personnel_categories"

    def get_queryset(self):
        return PersonnelCategory.objects.all()


class PersonnelCategoryUpdateView(DvzoUpdateView):
    permission_required = "train_management.change_personnelcategory"
    model = PersonnelCategory
    form_class = PersonnelCategoryForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("personnel-category-detail", kwargs={"pk": self.object.id})


class PersonnelCategoryCreateView(DvzoCreateView):
    permission_required = "train_management.add_personnelcategory"
    model = PersonnelCategory
    form_class = PersonnelCategoryForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("personnel-category-detail", kwargs={"pk": self.object.id})


class PersonnelCategoryDeleteView(DvzoDeleteView):
    permission_required = "train_management.delete_personnelcategory"
    model = PersonnelCategory
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("personnel-category-list")
