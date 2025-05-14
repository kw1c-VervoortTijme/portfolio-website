from django.utils.deprecation import MiddlewareMixin
from portfolio.translations import TRANSLATIONS

class LanguageDetectionMiddleware(MiddlewareMixin):
    """
    Middleware to detect and set the user's preferred language based on browser settings.
    """
    def process_request(self, request):
        # Only apply for users who don't have a language set in their session
        if 'language' not in request.session:
            # Get browser's Accept-Language header
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
            if accept_language:
                # Parse the Accept-Language header to get preferred languages
                languages = accept_language.split(',')
                for language in languages:
                    # Extract language code (strip quality value if present)
                    lang_code = language.split(';')[0].strip().lower()
                    # Look for a 2-letter language code
                    if '-' in lang_code:
                        lang_code = lang_code.split('-')[0]
                    
                    # Check if this language is supported
                    if lang_code in TRANSLATIONS:
                        request.session['language'] = lang_code
                        break
            
            # If no matching language found, set default
            if 'language' not in request.session:
                request.session['language'] = 'en'
        
        return None
