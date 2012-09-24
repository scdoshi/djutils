###############################################################################
## Imports
###############################################################################
# Django
from django import template
from django.forms.forms import BoundField

# User
from djutils.currency import currency_format

###############################################################################
## Code
###############################################################################
register = template.Library()


###############################################################################
## Filters
###############################################################################
@register.filter(name='currency2')
def currency2(dollars):
    try:
        dollars = float(dollars)
    except ValueError:
        return dollars

    # Convert to cents (integer)
    cents = int(dollars * 100)
    return currency_format(cents)


@register.filter(name='currency')
def currency(cents):
    return currency_format(cents)


class NamelessField(BoundField):
    def __init__(self, field):
        self.__dict__ = field.__dict__

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        """
        Renders the field by rendering the passed widget, adding any HTML
        attributes passed as attrs.  If no widget is specified, then the
        field's default widget will be used.
        """
        if not widget:
            widget = self.field.widget

        attrs = attrs or {}
        auto_id = self.auto_id
        if auto_id and 'id' not in attrs and 'id' not in widget.attrs:
            if not only_initial:
                attrs['id'] = auto_id
            else:
                attrs['id'] = self.html_initial_id

        name = ""
        return widget.render(name, self.value(), attrs=attrs)


@register.filter(name='namelessfield')
def namelessfield(field):
    return NamelessField(field)
