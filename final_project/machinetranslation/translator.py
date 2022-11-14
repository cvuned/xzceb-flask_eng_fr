"""
Translation package
Supported languages: English (en), French (fr)
"""

import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

VERSION = "2018-05-01"
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(englishtext):
    """
    This function translates English (en) to French (fr)
    """
    if englishtext == "":
        return ""
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
    return frenchtext.get("translations")[0].get("translation")

def french_to_english(frenchtext):
    """
    This function translates French (fr) to English (en)
    """
    if frenchtext == "":
        return ""
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
    return englishtext.get("translations")[0].get("translation")
