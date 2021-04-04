from django.forms import ModelForm

from train_management.models import TrainTimetableTemplate


class TrainTimetableTemplateForm(ModelForm):
    class Meta:
        model = TrainTimetableTemplate
        fields = ['template_name',
                  'label',
                  'comment',
                  'start_station',
                  'start_time',
                  'destination_station',
                  'destination_time',
                  ]
