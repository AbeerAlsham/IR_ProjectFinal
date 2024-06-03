import string

def remove_punctuation(corpus):
    punctuation_corpus = {}
    for doc_id, words in corpus.items():
        punctuation_corpus[doc_id] = list([word for word in words if word not in string.punctuation])
    return punctuation_corpus