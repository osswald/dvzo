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


class MiscArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = MiscArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'type'
        ]


class MiscFieldsetForm(TapeformFieldsetsMixin, MiscArticleForm):
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
                'type',),
        })


class ShirtArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ShirtArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'size'
        ]


class ShirtFieldsetForm(TapeformFieldsetsMixin, ShirtArticleForm):
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


class VestArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = VestArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'size'
        ]


class VestFieldsetForm(TapeformFieldsetsMixin, VestArticleForm):
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


class TieArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = TieArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'length'
        ]


class TieFieldsetForm(TapeformFieldsetsMixin, TieArticleForm):
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


class ShoesArticleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ShoesArticle
        fields = [
            'label',
            'status',
            'amount',
            'price',
            'size'
        ]


class ShoesFieldsetForm(TapeformFieldsetsMixin, ShoesArticleForm):
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
