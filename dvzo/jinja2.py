from django.utils.translation import gettext, ngettext
from jinja2 import Environment


def environment(**options):
    print("Setting environment stuff")
    # i18n extension
    options['extensions'] = ['jinja2.ext.i18n']

    # https://bandit.readthedocs.io/en/latest/plugins/b701_jinja2_autoescape_false.html
    # https://docs.djangoproject.com/en/3.2/topics/templates/#module-django.template.backends.django
    env = Environment(**options)  # nosec

    # i18n template functions
    env.install_gettext_callables(
        gettext=gettext,
        ngettext=ngettext,
        newstyle=True)

    return env
