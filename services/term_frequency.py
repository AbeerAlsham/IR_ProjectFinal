from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(corpus):
    vectorizer = TfidfVectorizer()
    corpus = convert_str(corpus)
    documents = list(corpus.values())
    tfidf_matrix = vectorizer.fit_transform(documents)  # Fit the vectorizer on the corpus
    return tfidf_matrix, vectorizer

def calculate_query_tfidf(query, vectorizer):
    query = convert_str(query)
    documents_query = list(query.values())
    tfidf_matrix_query = vectorizer.transform(documents_query)  # Transform the query
    return tfidf_matrix_query

def convert_str(corpus):
    str_corpus = {}
    for doc_id, words in corpus.items():
        str_words = " ".join(words)
        str_corpus[doc_id] = str_words
    return str_corpus