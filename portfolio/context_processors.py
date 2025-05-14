# portfolio/context_processors.py
from .translations import TRANSLATIONS

def translation_context(request):
    """
    Add translation context variables to templates.
    """
    # Get language from session or default to English
    current_language = request.session.get('language', 'en')
    
    return {
        'available_languages': list(TRANSLATIONS.keys()),
        'current_language': current_language,
    }
