import os

# Get the current working directory
current_directory = os.getcwd()

# Append the 'out' folder to the path
OUT_FOLDER = os.path.join(current_directory, 'out')

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
#              DATASETS             #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #


# antique dataset

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
ANTIQUE_DATASET_NOTPROCESSED_PATH = r"" # TSV file to be processed
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# Collection
ANTIQUE_DATASET_VECTORIZER_PATH =                   os.path.join(OUT_FOLDER, 'antique_collection_vectorizer.pkl')
ANTIQUE_DATASET_COLLECTION_PATH =                   os.path.join(OUT_FOLDER, 'antique_collection.pkl')
ANTIQUE_DATASET_COLLECTION_TFIDF_PATH =             os.path.join(OUT_FOLDER, 'antique_collection_tfidf.pkl')
ANTIQUE_DATASET_COLLECTION_INVERTED_INDEX_PATH =    os.path.join(OUT_FOLDER, 'antique_collection_inverted_index.pkl')

# Queries
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
ANTIQUE_QUERY_NOTPROCESSED_PATH = r"" # TSV file to be processed
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
ANTIQUE_TRAIN_QUERIES_VECTORIZER_PATH =           os.path.join(OUT_FOLDER, 'antique_query_vectorizer.pkl')
ANTIQUE_TRAIN_QUERIES_PATH =                      os.path.join(OUT_FOLDER, 'antique_query.pkl')
ANTIQUE_TRAIN_QUERIES_TFIDF_PATH =                os.path.join(OUT_FOLDER, 'antique_query_tfidf.pkl')
ANTIQUE_TRAIN_QUERIES_INVERTED_INDEX_PATH =       os.path.join(OUT_FOLDER, 'antique_query_inverted_index.pkl')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #


# lotte dataset

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
LOTTE_DATASET_NOTPROCESSED_PATH = r"" # TSV file to be processed
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# Collection
LOTTE_DATASET_VECTORIZER_PATH =                    os.path.join(OUT_FOLDER, 'lotte_collection_vectorizer.pkl')
LOTTE_DATASET_COLLECTION_PATH =                    os.path.join(OUT_FOLDER, 'lotte_collection.pkl')
LOTTE_DATASET_COLLECTION_TFIDF_PATH =              os.path.join(OUT_FOLDER, 'lotte_collection_tfidf.pkl')
LOTTE_DATASET_COLLECTION_INVERTED_INDEX_PATH =     os.path.join(OUT_FOLDER, 'lotte_collection_inverted_index.pkl')

# Queries
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
LOTTE_QUERY_NOTPROCESSED_PATH = r"" # TSV file to be processed
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
LOTTE_DATASET_QUERIES_VECTORIZER_PATH =            os.path.join(OUT_FOLDER, 'lotte_query_vectorizer.pkl')
LOTTE_DATASET_QUERIES_PATH =                       os.path.join(OUT_FOLDER, 'lotte_query.pkl')
LOTTE_DATASET_QUERIES_TFIDF_PATH =                 os.path.join(OUT_FOLDER, 'lotte_query_tfidf.pkl')
LOTTE_DATASET_QUERIES_INVERTED_INDEX_PATH =        os.path.join(OUT_FOLDER, 'lotte_query_inverted_index.pkl')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
