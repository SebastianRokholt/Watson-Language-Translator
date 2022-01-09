"""
This file contains the code for the instanciation of the Watson 
Language Translator API, as well as functions for translating 
strings to/from English to/from French.
"""

# Importing dependencies
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()


# Retrieving environment variables from .env
API_KEY = str(os.environ['apikey'])
URL = os.environ['url']

# IAM authentication for using the IBM Watson Language Translator API
authenticator = IAMAuthenticator(API_KEY)

# Instanciating the IBM Watson Language Translator API
language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(URL)


def english_to_french(english_text=""):
    """
    Translates from English to French.
    :param englishText: a string of at least a single word
    """
    if english_text == "":
        print("Please provide a text string of at least one word as input.")
        return None

    french_result = language_translator.translate(
        english_text, model_id="en-fr")
    french_text = french_result._to_dict(
    )["result"]["translations"][0]["translation"]
    return french_text


# Translates from French to English
def french_to_english(french_text=""):
    """
    Translates from French to English.
    :param englishText: a string of at least a single word
    """
    if french_text == "":
        print("Please provide a text string of at least one word as input.")
        return None

    english_result = language_translator.translate(
        french_text, model_id="fr-en")
    english_text = english_result._to_dict(
    )["result"]["translations"][0]["translation"]
    return english_text


# # Test
# if __name__ == "__main__":
#     en_text = "I want to ride my bicycle, I want to ride my bike!"
#     print("Translated to French: ", english_to_french(en_text))

#     fr_text = english_to_french(en_text)
#     print("Translated to English: ", french_to_english(fr_text))