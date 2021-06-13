from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin
from tapeforms.fieldsets import TapeformFieldsetsMixin

from train_management.models import DayPlanning


class DayPlanningForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = DayPlanning
        fields = ['label',
                  'date',
                  'day_planning_type',
                  'status',
                  'paid',
                  'text',
                  'slot_ordered',
                  'personnel_disposition',
                  'customers',
                  'price',
                  'booking_status',
                  'comment'
                  ]
    date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d')
    )


class DayPlanningFieldsetForm(TapeformFieldsetsMixin, DayPlanningForm):
    fieldsets = (
        {
            'extra': {
                'title': _("form.dayplanning.master_data"),
                'css_class': 'csssss'
            },
            'fields': (
                'label',
                'date',
                'day_planning_type',
                'status',
                'text'),
        }, {
            'extra': {
                'title': _("form.dayplanning.planning"),
                'css_class': 'csssss',
            },
            'fields': (
                'slot_ordered',
                'personnel_disposition'),
        }, {
            'extra': {
                'title': _("form.dayplanning.booking"),
                'css_class': 'csssss',
            },
            'fields': (
                'booking_status',
                'customers',
                'price',
                'paid'),
        })
