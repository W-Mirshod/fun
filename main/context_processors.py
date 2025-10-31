import os


def main_character_processor(request):
    """Context processor to make main_character available in all templates."""
    return {
        'main_character': os.environ.get('main_character', 'Orange')
    }
