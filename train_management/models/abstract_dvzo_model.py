from django.db import models
from django.utils.translation import gettext_lazy as _
from django_currentuser.db.models import CurrentUserField


class AbstractDvzoModel(models.Model):
    create_user = CurrentUserField(related_name='created_%(class)ss')
    create_timestamp = models.DateTimeField(_("create_timestamp"), auto_now_add=True, null=True)
    update_user = CurrentUserField(on_update=True, related_name='updated_%(class)ss')
    update_timestamp = models.DateTimeField(_("update_timestamp"), auto_now=True, null=True)

    class Meta:
        abstract = True
