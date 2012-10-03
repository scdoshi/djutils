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

    if negative:
        return "- $%s.%s" % (intcomma(dollars), str(cents))
    return "$%s.%s" % (intcomma(dollars), str(cents))
