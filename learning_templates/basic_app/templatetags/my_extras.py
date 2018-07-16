from django import template

register = template.Library()

@register.filter(name='cut')
def cut(valur,arg):
    """
    This cutss out all value of "arg" from the string
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
