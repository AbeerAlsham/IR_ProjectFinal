from configuration import config

ANTIQUE_TRAIN_QUERIES_VECTORIZER = None
ANTIQUE_TRAIN_QUERIES = None
ANTIQUE_TRAIN_QUERIES_TFIDF = None
ANTIQUE_TRAIN_QUERIES_INVERTED_INDEX = None

LOTTE_TRAIN_QUERIES_VECTORIZER = None
LOTTE_TRAIN_QUERIES = None
LOTTE_TRAIN_QUERIES_TFIDF = None
LOTTE_TRAIN_QUERIES_INVERTED_INDEX = None

def query_collection():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_TRAIN_QUERIES
    else:
        return LOTTE_TRAIN_QUERIES

def query_collection_tfidf():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_TRAIN_QUERIES_TFIDF
    else:
        return LOTTE_TRAIN_QUERIES_TFIDF
    
def query_collection_inverted_index():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_TRAIN_QUERIES_INVERTED_INDEX
    else:
        return LOTTE_TRAIN_QUERIES_INVERTED_INDEX
    
    
def queries_tfidf_vectorizer():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_TRAIN_QUERIES_VECTORIZER
    else:
        return LOTTE_TRAIN_QUERIES_VECTORIZER