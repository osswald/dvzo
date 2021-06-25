from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoTemplateView, DvzoUpdateView
from train_management.forms import PhoneNumberForm
from train_management.models import Personnel, PhoneNumber


class PhoneNumberListView(DvzoListView):
    permission_required = 'train_management.view_phonenumber'
    context_object_name = "phone_numbers"

    def get_queryset(self):
        return PhoneNumber.objects.all()


class PhoneNumberUpdateView(DvzoUpdateView):
    permission_required = 'train_management.change_phonenumber'
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("phone-detail", kwargs={'pk': self.object.id})


class PhoneNumberCreateView(DvzoCreateView):
    permission_required = 'train_management.add_phonenumber'
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("phone-detail", kwargs={'pk': self.object.id})


class PhoneNumberDeleteView(DvzoDeleteView):
    permission_required = 'train_management.delete_phonenumber'
    model = PhoneNumber
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("phone-list")


class PhoneNumberOverview(DvzoTemplateView):
    permission_required = ''
    template_name = "train_management/phonenumber_overview.html"


class PhoneNumberDetail(DvzoListView):
    permission_required = ''

    def get_queryset(self):
        return PhoneNumber.objects.filter(phone_number_type=self.request.GET['type']).order_by("label")
    template_name = "train_management/phonenumber_type.html"
    context_object_name = "phone_numbers"


class PhoneNumberMemberList(DvzoListView):
    permission_required = ''
    queryset = Personnel.objects.filter(status="active", mobile_phone_public="yes")\
        .exclude(mobile_phone="").order_by("user__last_name")
    template_name = "train_management/phonenumber_member.html"
    context_object_name = "phone_numbers"
