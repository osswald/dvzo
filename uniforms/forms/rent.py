from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from uniforms.models import ArticleRent, Rent


class RentForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Rent
        fields = ['renter',
                  'start',
                  'end',
                  'returned',
                  'billed',
                  ]


class ArticleRentForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ArticleRent
        fields = ['article',
                  'amount',
                  ]