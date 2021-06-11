import functools
import ssl

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.utils import django_url_fetcher
from django_weasyprint.views import WeasyTemplateResponse

from uniforms.views import LetDetailView, RentDetailView


class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)


class RentPdfView(WeasyTemplateResponseMixin, RentDetailView):
    pdf_attachment = False
    response_class = CustomWeasyTemplateResponse


class LetPdfView(WeasyTemplateResponseMixin, LetDetailView):
    pdf_attachment = False
    response_class = CustomWeasyTemplateResponse
