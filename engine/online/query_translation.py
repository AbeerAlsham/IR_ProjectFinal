from configuration import config
from services import translator

def translate_query(query, language, spellcheck):
    if language is not None and language in [config.LANG_ENGLISH, config.LANG_OTHER]:
        config.SELECTED_LANGUAGE = language
        
    if spellcheck is not None and spellcheck in [config.NO_SPELLCHECK, config.OFFLINE_SPELLCHECK, config.ONLINE_SPELLCHECK]:
        config.SELCTED_SPELLCHECK_OPTION = spellcheck
        
    result = query
    if (config.SELECTED_LANGUAGE == config.LANG_OTHER) or (config.SELCTED_SPELLCHECK_OPTION == config.ONLINE_SPELLCHECK):
        result =  translator.translate(query)
        
    return result