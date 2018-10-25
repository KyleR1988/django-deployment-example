from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')

# To register the filter use register.filter('filter_name', filter)
# register.filter('cut', cut)
