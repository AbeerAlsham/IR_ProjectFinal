from scipy.sparse import vstack

def get_matched_documents(processed_query, inverted_index):
    matched_documents = set()
    for token in processed_query:
        if token in inverted_index:
            docs_idxs = inverted_index[token]
            for doc_idx in docs_idxs:
                matched_documents.add(doc_idx)
    return matched_documents

def get_matched_matrix(docs_tfidf, matched_documents):
    matched_rows = [docs_tfidf.getrow(doc_idx) for doc_idx in matched_documents]
    matched_matrix = vstack(matched_rows)
    return matched_matrix

def get_documents(corpus, result_idxs):
    # Create a list of document IDs in the same order as the documents in the TF-IDF matrix
    doc_ids = list(corpus.keys())
    # Use the indices to get the corresponding document IDs, and then get the documents from the corpus
    return [corpus[doc_ids[idx]] for idx in result_idxs]