from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoUpdateView
from train_management.forms import PersonnelForm, UserForm
from train_management.models import Personnel


class PersonnelListView(DvzoListView):
    permission_required = 'train_management.view_personnel'
    model = Personnel
    context_object_name = "personnels"

    def get_queryset(self):
        return Personnel.objects.all()


class PersonnelUpdateView(DvzoUpdateView):
    permission_required = 'train_management.change_personnel'
    model = Personnel
    form_class = PersonnelForm
    template_name_suffix = "_update_form"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        user_form = UserForm(request.POST, instance=self.object.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(user_form=user_form, form=form)

    def form_invalid(self, **kwargs):
        print("test", kwargs["form"].instance.id)
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        if "user_form" not in kwargs:
            kwargs["user_form"] = UserForm(instance=self.object.user)
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy("personnel-list")


class PersonnelCreateView(DvzoCreateView):
    permission_required = 'train_management.add_personnel'
    model = Personnel
    form_class = PersonnelForm
    template_name_suffix = "_create_form"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user_form = self.get_form(UserForm)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            form.instance.user_id = user.id
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            return self.form_invalid(user_form=user_form, form=form)

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            kwargs["form"] = PersonnelForm()
        if "user_form" not in kwargs:
            kwargs["user_form"] = UserForm()
        return kwargs

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_success_url(self):
        return reverse_lazy("personnel-list")


class PersonnelDeleteView(DvzoDeleteView):
    permission_required = 'train_management.delete_personnel'
    model = Personnel
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("personnel-list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        success_url = self.get_success_url()
        self.object.delete()
        user.delete()
        return HttpResponseRedirect(success_url)
