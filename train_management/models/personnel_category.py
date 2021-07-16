from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class PersonnelCategory(AbstractDvzoModel):
    class Meta:
        verbose_name = _("personnel_category.singular")
        verbose_name_plural = _("personnel_category.plural")

    class PersonnelCategoryType(models.TextChoices):
        ENGINE = "engine", _("personnel_category.type.engine")
        TRAIN = "train", _("personnel_category.type.train")
        GASTRO = "gastro", _("personnel_category.type.gastro")
        STATION = "station", _("personnel_category.type.station")
        OTHER = "other", _("personnel_category.type.other")

    label = models.CharField(_("personnel_category.label"), max_length=200)
    type = models.CharField(_("personnel_category.type"), max_length=80, choices=PersonnelCategoryType.choices)

    def __str__(self):
        return self.label
