from django.db import models
from django.utils.translation import gettext_lazy as _

from shifts.models import ShiftTemplate
from train_management.models import AbstractDvzoModel, FunctionPersons, Station


class ShiftPositionType(AbstractDvzoModel):

    class Meta:
        verbose_name = _("shift_position_type.singular")
        verbose_name_plural = _("shift_position_type.plural")

    label = models.CharField(_("shift_position.label"), max_length=200)
    work_time = models.BooleanField(_("shift_position_type.work_time"), default=True)

    def __str__(self):
        return self.label


class ShiftPosition(AbstractDvzoModel):

    class Meta:
        verbose_name = _("shift_position.singular")
        verbose_name_plural = _("shift_position.plural")

    label = models.CharField(_("shift_position.label"), max_length=200)
    type = models.ForeignKey(ShiftPositionType, on_delete=models.CASCADE)
    start_time = models.TimeField(_("shift_position.start_time"))
    end_time = models.TimeField(_("shift_position.end_time"))
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="shift_position_start_station",
                                      null=True, blank=True)
    end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="shift_position_end_station",
                                    null=True, blank=True)
    template = models.ForeignKey(ShiftTemplate, on_delete=models.CASCADE, null=True, blank=True)
    function_persons = models.ForeignKey(FunctionPersons, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.label
