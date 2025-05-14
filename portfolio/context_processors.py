# portfolio/context_processors.py

from .translations import translate, TRANSLATIONS

def translation_context(request):
    """
    Add translation function and available languages to the template context.
    """
    current_language = request.session.get('language', 'en')
    
    return {
        'translate': lambda key: translate(key, current_language),
        'available_languages': list(TRANSLATIONS.keys()),
        'current_language': current_language,
    }
