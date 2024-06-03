from services import text_normalizer
from services import tokenizer
from services import punctuation_remover
from services import lemmatizer
from services import stop_words_remover

def process_document(corpus):
    #text normalizer
    normalized_document = text_normalizer.normalize_text(corpus)
    
    #tokenize query
    tokenized_document = tokenizer.tokenize(normalized_document)
    
    #remove punctuation
    non_punctuation_document = punctuation_remover.remove_punctuation(tokenized_document)
    
    #lemmetizing
    lemmatized_document = lemmatizer.lemmatize(non_punctuation_document)
    
    #remove stop words
    non_stopwords_document = stop_words_remover.remove_stopwords(lemmatized_document)
    
    return non_stopwords_document
