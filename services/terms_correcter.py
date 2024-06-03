from spellchecker import SpellChecker

spell = SpellChecker()

def correct_terms(tokenized_text):
    if not tokenized_text:
        return {}
    corrected_corpus = {}
    for doc_id, tokens in tokenized_text.items():
        corrected_terms = [spell.correction(term) if spell.correction(term) else term for term in tokens]
        corrected_corpus[doc_id] = corrected_terms
    return corrected_corpus