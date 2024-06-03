from services import duplicate_remover
from services import inverted_index
from services import term_frequency


def document_representation(corpus):
    # Calculate Fit corpus vectorizer
    tfidf_df, vectorizer = term_frequency.calculate_tfidf(corpus)
    
    # Create inverted index
    inverted_index_document = inverted_index.create_inverted_index(corpus)
    
    return inverted_index_document, tfidf_df, vectorizer