import functools
import ssl

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.utils import django_url_fetcher
from django_weasyprint.views import WeasyTemplateResponse

from train_management.views import DayPlanningBulletinView
from train_management.views import DayPlanningDetailView


class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)


class BriefingPrintView(WeasyTemplateResponseMixin, DayPlanningDetailView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    response_class = CustomWeasyTemplateResponse


class BulletinPrintView(WeasyTemplateResponseMixin, DayPlanningBulletinView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # custom response class to configure url-fetcher
    response_class = CustomWeasyTemplateResponse
