from datasource import docs, queries
from services import io
from configuration import paths

def load():
    # Antique
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
    queries.ANTIQUE_TRAIN_QUERIES_VECTORIZER = io.read_object_from_file(paths.ANTIQUE_TRAIN_QUERIES_VECTORIZER_PATH)
    queries.ANTIQUE_TRAIN_QUERIES = io.read_object_from_file(paths.ANTIQUE_TRAIN_QUERIES_PATH)
    queries.ANTIQUE_TRAIN_QUERIES_TFIDF = io.read_object_from_file(paths.ANTIQUE_TRAIN_QUERIES_TFIDF_PATH)
    queries.ANTIQUE_TRAIN_QUERIES_INVERTED_INDEX = io.read_object_from_file(paths.ANTIQUE_TRAIN_QUERIES_INVERTED_INDEX_PATH)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
    docs.ANTIQUE_DATASET_VECTORIZER = io.read_object_from_file(paths.ANTIQUE_DATASET_VECTORIZER_PATH)
    docs.ANTIQUE_DATASET_COLLECTION = io.read_object_from_file(paths.ANTIQUE_DATASET_COLLECTION_PATH)
    docs.ANTIQUE_DATASET_COLLECTION_TFIDF = io.read_object_from_file(paths.ANTIQUE_DATASET_COLLECTION_TFIDF_PATH)
    docs.ANTIQUE_DATASET_COLLECTION_INVERTED_INDEX = io.read_object_from_file(paths.ANTIQUE_DATASET_COLLECTION_INVERTED_INDEX_PATH)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
    
    # Lotte
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
    queries.LOTTE_DATASET_QUERIES_VECTORIZER = io.read_object_from_file(paths.LOTTE_DATASET_QUERIES_VECTORIZER_PATH)
    queries.LOTTE_DATASET_QUERIES = io.read_object_from_file(paths.LOTTE_DATASET_QUERIES_PATH)
    queries.LOTTE_DATASET_QUERIES_TFIDF = io.read_object_from_file(paths.LOTTE_DATASET_QUERIES_TFIDF_PATH)
    queries.LOTTE_DATASET_QUERIES_INVERTED_INDEX = io.read_object_from_file(paths.LOTTE_DATASET_QUERIES_INVERTED_INDEX_PATH)
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
    docs.LOTTE_DATASET_VECTORIZER = io.read_object_from_file(paths.LOTTE_DATASET_VECTORIZER_PATH)
    docs.LOTTE_DATASET_COLLECTION = io.read_object_from_file(paths.LOTTE_DATASET_COLLECTION_PATH)
    docs.LOTTE_DATASET_COLLECTION_TFIDF = io.read_object_from_file(paths.LOTTE_DATASET_COLLECTION_TFIDF_PATH)
    docs.LOTTE_DATASET_COLLECTION_INVERTED_INDEX = io.read_object_from_file(paths.LOTTE_DATASET_COLLECTION_INVERTED_INDEX_PATH)