from engine.online import query_text_processor
from engine.online import query_representer
from engine.online import query_matcher
from engine.online import rank_documents
from engine.online import query_translation
from datasource import docs
from configuration import config

def search_doc(query, dataset, language, spellcheck):
    # Set Dataset if passed
    if dataset is not None and dataset in [config.ANTIQUE_DATASET, config.LOTTE_DATASET]:
        config.SELECTED_DATASET = dataset
        
    # Translate the query
    translated_query = query_translation.translate_query(query, language, spellcheck)
    
     # Forming the query
    query = { "query" : translated_query }
    
    # Process the query
    processed_query = query_text_processor.process_query(query)

    # If the processed query is empty, return an empty list
    if not any(processed_query.values()):
        return []

    # Query inverted index & TF-IDF DataFrame
    query_tfidf_df = query_representer.query_representation(processed_query, docs.dataset_tfidf_vectorizer())
    
    # Get loaded documents inverted index
    dataset_inverted_index = docs.dataset_collection_inverted_index()
    
    # Get the documents that match the query
    matched_documents = query_matcher.get_matched_documents(processed_query['query'], dataset_inverted_index)
    
    # If no documents match the query, return an empty list
    if not matched_documents:
        return []
    
    # Get loaded dataset documents TF-IDF DataFrame here
    dataset_tfidf_df = docs.dataset_collection_tfidf()
    
    # Rank the documents based on their relevance to the query
    ranked_docs_idx = rank_documents.rank(query_tfidf_df, dataset_tfidf_df, matched_documents, config.DOCUEMENTS_SEARCH_RETRIEVE_COUNT)
    
    # Get selected corpus
    corpus = docs.dataset_collection()
    
    # Get documents corresponded idx
    result = query_matcher.get_documents(corpus, ranked_docs_idx)
    
    return result