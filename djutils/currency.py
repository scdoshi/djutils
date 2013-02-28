"""
Currency: This module is for currency related utilites.

Module elements not in this file:
1. `currency` and `currency2` filters: to use the format function in
      templates. Located in djutils.templatetags.custom_utils

"""

###############################################################################
## Imports
###############################################################################
# Django
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models


# Extenal
if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^djutils\.currency\.CurrencyField"])


###############################################################################
## Fields
###############################################################################
class CurrencyField(models.IntegerField):
    """Placeholder for CurrencyField. Add custom behaviour later. """
    pass


###############################################################################
## Formatting
###############################################################################
def currency_format(cents):
    try:
        cents = int(cents)
    except ValueError:
        return cents

    negative = False
    if cents < 0:
        cents = -1 * cents
        negative = True

    if cents < 100:
        dollars = 0
    else:
        dollars = cents / 100
        cents = cents % 100

    centstr = str(cents)
    if len(centstr) < 2:
        centstr = '0' + centstr

    if negative:
        return "- $%s.%s" % (intcomma(dollars), centstr)
    return "$%s.%s" % (intcomma(dollars), centstr)
