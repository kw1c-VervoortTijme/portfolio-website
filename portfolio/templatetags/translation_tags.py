from django import template
from portfolio.translations import translate, TRANSLATIONS

register = template.Library()

@register.simple_tag(takes_context=True)
def t(context, key):
    """
    Template tag to translate text keys.
    Usage: {% t 'home_title' %}
    """
    request = context.get('request')
    language = request.session.get('language', 'en') if request else 'en'
    return translate(key, language)


@register.simple_tag
def get_language_name(code):
    """
    Return the name of the language given its code.
    Usage: {% get_language_name 'en' %}
    """
    return code.upper()
