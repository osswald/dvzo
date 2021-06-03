from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class CopyRecipient(AbstractDvzoModel):
    class Meta:
        verbose_name = _("copy_recipient.singular")
        verbose_name_plural = _("copy_recipient.plural")

    label = models.CharField(_("copy_recipient.label"), max_length=200)
    email = models.EmailField(_("copy_recipient.email"), blank=True)

    def __str__(self):
        return self.label
