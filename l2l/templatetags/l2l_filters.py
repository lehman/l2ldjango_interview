from django import template
from datetime import datetime
# from dateutil import parser

register = template.Library()
@register.filter
def toDateAndTimeString(value):
    """
    Input: Either:
           - a date object
           - a string in the following format: "%Y-%m-%dT%H:%M:%S"
           
    Returns: The input value in the following format: "%Y-%m-%d %H:%M:%S"
    """
    asDatetimeObject = value
    if isinstance(value, str):
        # convert from string to datetime object first
        asDatetimeObject = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")

        # here is another more flexible solution that would work
        # with strings in more formats than "%Y-%m-%dT%H:%M:%S"
        # asDatetimeObject = parser.parse(value)
    formattedString = asDatetimeObject.strftime("%Y-%m-%d %H:%M:%S")
    return formattedString
