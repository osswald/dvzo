from django.forms import ModelForm

from train_management.models import DayPlanning


class DayPlanningForm(ModelForm):
    class Meta:
        model = DayPlanning
        fields = ['label', 'date', 'day_planning_type', 'status', 'paid', 'text']
