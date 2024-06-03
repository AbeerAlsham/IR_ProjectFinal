from googletrans import Translator

# init the Google API translator
translator = Translator()

def translate(query):
    translation = translator.translate(query, dest="en")
    return translation.text