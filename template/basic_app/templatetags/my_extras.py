from django import template

register=template.Library()
@register.filter(name='cut')
def cut(value,arg):

    """
    cuts argument
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
