"""
Attribute Lookup: Lookup attributes in django templates dynamically

"""

###############################################################################
## Imports
###############################################################################
from django import template
from django.template import Variable, VariableDoesNotExist


###############################################################################
## Filters
###############################################################################
register = template.Library()


@register.filter(name='attr')
def attr(object, attr):
    """
    Lookup attributes in django templates dynamically
    From http://stackoverflow.com/a/3466349/594269

    Allows lookups such as {{ user|attr:item }} where item is a
    template variable
    """
    pseudo_context = {'object': object}
    try:
        value = Variable('object.%s' % attr).resolve(pseudo_context)
    except VariableDoesNotExist:
        value = None
    return value
