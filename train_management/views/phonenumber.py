from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import TemplateView

from train_management.forms import PhoneNumberForm
from train_management.models import Personnel, PhoneNumber


@method_decorator(login_required, name='dispatch')
class PhoneNumberListView(generic.ListView):
    context_object_name = "phone_numbers"

    def get_queryset(self):
        return PhoneNumber.objects.all()


@method_decorator(login_required, name='dispatch')
class PhoneNumberUpdateView(generic.UpdateView):
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("phone-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PhoneNumberCreateView(generic.CreateView):
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("phone-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PhoneNumberDeleteView(generic.DeleteView):
    model = PhoneNumber
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("phone-list")


@method_decorator(login_required, name='dispatch')
class PhoneNumberOverview(TemplateView):
    template_name = "train_management/phonenumber_overview.html"


@method_decorator(login_required, name='dispatch')
class PhoneNumberDetail(generic.ListView):

    def get_queryset(self):
        return PhoneNumber.objects.filter(phone_number_type=self.request.GET['type']).order_by("label")
    template_name = "train_management/phonenumber_type.html"
    context_object_name = "phone_numbers"


@method_decorator(login_required, name='dispatch')
class PhoneNumberMemberList(generic.ListView):
    queryset = Personnel.objects.filter(status="active", mobile_phone_public=True).order_by("user__last_name")
    template_name = "train_management/phonenumber_member.html"
    context_object_name = "phone_numbers"
