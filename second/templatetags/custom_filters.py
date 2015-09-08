__author__ = 'Manuel'

from django import template

register = template.Library()

@register.simple_tag
def fecha_actual():
    from datetime import datetime
    current_site = datetime.today()

    return current_site

@register.filter
def dollar(value):
    return "$" + str(value)



@register.filter
def adjust(value, arg):
    """Adjusts the datetime object by the argument and returns the new datetime for formatting

      @note: Uses relativedelta to adjust the date object

      Usage: {{ dateobject|adjust:"weeks=1" }}, or
             {{ dateobject|adjust:"weeks=1, days=2"|date:"Y m d" }}
    """
    from dateutil.relativedelta import relativedelta
    args = dict(tuple(e.split('=')) for e in arg.split(', '))

    for k, v in args.iteritems():
        args[k] = int(v) # Convert all values to integers

    return value + relativedelta(**args)