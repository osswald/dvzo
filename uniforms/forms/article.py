from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin
from tapeforms.fieldsets import TapeformFieldsetsMixin

from uniforms.models import (CoatArticle, HatArticle, MiscArticle, ShirtArticle, ShoesArticle, VestArticle,
                             TieArticle, TrousersArticle)


class CoatArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = CoatArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'size'
        ]


class CoatFieldsetForm(TapeformFieldsetsMixin, CoatArticleForm):
    fieldsets = (
        {
            'extra': {
                'title': _("form.master_data"),
                'css_class': 'csssss'
            },
            'fields': (
                'label',
                'status',
                'amount',
                'price'),
        }, {
            'extra': {
                'title': _("form.special_fields"),
                'css_class': 'csssss',
            },
            'fields': (
                'size',),
        })


class HatArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = HatArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'circumference'
        ]


class HatFieldsetForm(TapeformFieldsetsMixin, HatArticleForm):
    fieldsets = (
        {
            'extra': {
                'title': _("form.master_data"),
                'css_class': 'csssss'
            },
            'fields': (
                'label',
                'status',
                'amount',
                'price'),
        }, {
            'extra': {
                'title': _("form.special_fields"),
                'css_class': 'csssss',
            },
            'fields': (
                'circumference',),
        })


class TrousersArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = TrousersArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'waist',
            'length'
        ]


class TrousersFieldsetForm(TapeformFieldsetsMixin, TrousersArticleForm):
    fieldsets = (
        {
            'extra': {
                'title': _("form.master_data"),
                'css_class': 'csssss'
            },
            'fields': (
                'label',
                'status',
                'amount',
                'price'),
        }, {
            'extra': {
                'title': _("form.special_fields"),
                'css_class': 'csssss',
            },
            'fields': (
                'size',
                'waist',
                'length',
            ),
        })
