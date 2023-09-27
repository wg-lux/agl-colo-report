from django import template

register = template.Library()

@register.filter(name='is_in')
def is_in(value, arg):
    return value in arg.split(',')

@register.filter
def get_item(list, index):
    return list[index]