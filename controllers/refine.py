from engine.online import query_text_processor
from engine.online import query_representer
from engine.online import query_matcher
from engine.online import rank_documents
from datasource import queries
from configuration import config


# It is only supported english right now
def suggest(query, dataset, language = None):
    # Set Dataset if passed
    if dataset is not None and dataset in [config.ANTIQUE_DATASET, config.LOTTE_DATASET]:
        config.SELECTED_DATASET = dataset

     # Forming the query
    query = { "query" : query }
    
    # Process the query
    processed_query = query_text_processor.process_query(query)
    
    # If the processed query is empty, return an empty list
    if not any(processed_query.values()):
        return []

    # Query inverted index & TF-IDF DataFrame
    query_tfidf_df = query_representer.query_representation(processed_query, queries.queries_tfidf_vectorizer())
    
    # Get loaded queries inverted index
    inverted_index = queries.query_collection_inverted_index()
    
    # Get the queries suggestions that match the query
    matched_queries = query_matcher.get_matched_documents(processed_query['query'], inverted_index)

    # If no query suggestion match the query, return an empty list
    if not matched_queries:
        return []
    
    # Get loaded queries documents TF-IDF
    queries_tfidf_df = queries.query_collection_tfidf()
    
    # Rank the documents based on their relevance to the query
    ranked_queries_idx = rank_documents.rank(query_tfidf_df, queries_tfidf_df, matched_queries, config.QUERY_SUGGESTION_RETRIEVE_COUNT)
    
    # Get selected corpus
    corpus = queries.query_collection()
    
    result = query_matcher.get_documents(corpus, ranked_queries_idx)
    
    # Return the ranked list of documents
    return result