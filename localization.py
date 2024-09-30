# localization.py
import gettext
import os
import config

def setup_localization(language='en'):
    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    try:
        translate = gettext.translation('renamer', localedir, languages=[language], fallback=True)
        translate.install()
        return translate.gettext
    except Exception as e:
        print(f"Warning: Error setting up translation for language '{language}': {e}")
        return lambda x: x  # Returnează o funcție care returnează textul neschimbat

# Funcția de traducere implicită
_ = setup_localization(config.language)