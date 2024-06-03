from services import term_frequency

def query_representation(corpus, vectorizer):
    query_tfidf = term_frequency.calculate_query_tfidf(corpus, vectorizer)
    return query_tfidf