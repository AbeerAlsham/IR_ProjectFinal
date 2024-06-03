from configuration import config

ANTIQUE_DATASET_VECTORIZER = None
ANTIQUE_DATASET_COLLECTION = None
ANTIQUE_DATASET_COLLECTION_TFIDF = None
ANTIQUE_DATASET_COLLECTION_INVERTED_INDEX = None


LOTTE_DATASET_VECTORIZER = None
LOTTE_DATASET_COLLECTION = None
LOTTE_DATASET_COLLECTION_TFIDF = None
LOTTE_DATASET_COLLECTION_INVERTED_INDEX = None


def dataset_collection():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_DATASET_COLLECTION
    else:
        return LOTTE_DATASET_COLLECTION

def dataset_collection_tfidf():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_DATASET_COLLECTION_TFIDF
    else:
        return LOTTE_DATASET_COLLECTION_TFIDF
    
    
def dataset_collection_inverted_index():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_DATASET_COLLECTION_INVERTED_INDEX
    else:
        return LOTTE_DATASET_COLLECTION_INVERTED_INDEX


def dataset_tfidf_vectorizer():
    if(config.SELECTED_DATASET == config.ANTIQUE_DATASET):
        return ANTIQUE_DATASET_VECTORIZER
    else:
        return LOTTE_DATASET_VECTORIZER