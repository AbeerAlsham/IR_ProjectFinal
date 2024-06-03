from services import text_normalizer
from services import terms_correcter
from services import tokenizer
from services import punctuation_remover
from services import lemmatizer
from services import stop_words_remover
from configuration import config

def process_query(corpus):
    #text normalizer
    normalized_query = text_normalizer.normalize_text(corpus)
    
    #tokenize query
    tokenized_query = tokenizer.tokenize(normalized_query)
    
    #terms correction
    if(config.SELCTED_SPELLCHECK_OPTION == config.OFFLINE_SPELLCHECK):
        tokenized_query = terms_correcter.correct_terms(tokenized_query)
    
    #remove punctuation
    non_punctuation_query = punctuation_remover.remove_punctuation(tokenized_query)
    
    #lemmetizing
    lemmatized_query = lemmatizer.lemmatize(non_punctuation_query)
    
    #remove stop words
    non_stopwords_query = stop_words_remover.remove_stopwords(lemmatized_query)
    
    return non_stopwords_query