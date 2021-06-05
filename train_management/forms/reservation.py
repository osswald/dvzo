from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Reservation


class ReservationForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Reservation
        fields = ['label',
                  'phone',
                  'email',
                  'amount',
                  'start',
                  'end',
                  'reservation_type',
                  'reservation_status',
                  'comment',
                  ]
