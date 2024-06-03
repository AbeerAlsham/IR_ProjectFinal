from sklearn.metrics.pairwise import cosine_similarity
from engine.online import query_matcher

def rank(query_tfidf, docs_tfidf, matched_documents, doc_count):
    # Get the TF-IDF vectors for the matched documents
    matched_matrix = query_matcher.get_matched_matrix(docs_tfidf, matched_documents)
    
    # Calculate the cosine similarity between the query and the matched documents
    result = get_cosine_similarity(query_tfidf, matched_matrix)
    
    # Sort the results by similarity score
    result_with_idx = sort_results(result)
    
    # Get the indices of the top results
    result_idxs = get_top_results(result_with_idx, doc_count)
    
    # Convert the indices to document IDs
    result_doc_ids = [list(matched_documents)[idx] for idx in result_idxs]
    
    return result_doc_ids


def get_cosine_similarity(query_tfidf, matched_matrix):
    result = cosine_similarity(query_tfidf, matched_matrix).flatten()
    return result

def sort_results(result):
    result_with_idx = sorted(enumerate(result), key=lambda x: x[1], reverse=True)
    return result_with_idx

def get_top_results(result_with_idx, doc_count):
    result_idxs = [result_with_idx[j][0] for j in range(min(doc_count, len(result_with_idx)))]
    return result_idxs