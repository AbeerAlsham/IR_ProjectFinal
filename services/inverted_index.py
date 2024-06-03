from scipy.sparse import lil_matrix, find
from datasource import docs

def create_inverted_index(tfidf_matrix):
    # get the number of documents and terms
    num_docs = tfidf_matrix.shape[0]
    num_terms = tfidf_matrix.shape[1]

    # create an empty lil_matrix with the same shape as the tfidf matrix
    inverted_index = lil_matrix((num_terms, num_docs), dtype=int)

    # get the row indices, column indices and values of the non-zero entries
    row_indices, col_indices, _ = find(tfidf_matrix)

    # loop over the non-zero entries
    for doc_index, word_index in zip(row_indices, col_indices):
        # add the document ID to the corresponding entry in the lil_matrix
        inverted_index[word_index, doc_index] = 1

    # convert the lil_matrix to a csr_matrix for efficient arithmetic and matrix operations
    inverted_index = inverted_index.tocsr()

    vectorizer = docs.dataset_tfidf_vectorizer()
    
    # convert inverted index to dictionary
    inverted_index_dict = {}
    terms = vectorizer.get_feature_names_out()

    # iterate over the non-zero elements of the sparse matrix
    for term_index, doc_index in zip(*inverted_index.nonzero()):
        term = terms[term_index]
        if term not in inverted_index_dict:
            inverted_index_dict[term] = []
        inverted_index_dict[term].append(doc_index)

    return inverted_index_dict