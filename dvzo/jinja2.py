from django.utils.translation import gettext, ngettext
from jinja2 import Environment


def environment(**options):
    print("Setting environment stuff")
    # i18n extension
    options['extensions'] = ['jinja2.ext.i18n']

    env = Environment(**options)

    # i18n template functions
    env.install_gettext_callables(
        gettext=gettext,
        ngettext=ngettext,
        newstyle=True)

    return env
