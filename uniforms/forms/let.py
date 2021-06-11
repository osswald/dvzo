from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from uniforms.models import ArticleLet, Let


class LetForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Let
        fields = ['personnel',
                  'start',
                  'end',
                  'returned',
                  ]


class ArticleLetForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ArticleLet
        fields = ['article',
                  'amount',
                  ]
