from django import template
from datetime import datetime


register = template.Library()

_from_format = "%Y-%m-%dT%H:%M:%S"
_into_format = "%Y-%m-%d %H:%M:%S"

# Return empty string just as django built in filters do when bad input
# is given. Such as floatformat, dicsort and others

@register.filter(name="l2l_dt")
def format_date(value):
    """Format a date to a L2L specific format. If bad input, empty string."""
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, _from_format)
        except ValueError:
            return ""
    if not isinstance(value, datetime):
        return ""

    return value.strftime(_into_format)
