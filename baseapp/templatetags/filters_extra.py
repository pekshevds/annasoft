from django import template
register = template.Library()

def remove_spaces(value):
    return value.replace(' ', '')

register.filter('remove_spaces', remove_spaces)