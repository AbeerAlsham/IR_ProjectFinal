from nltk.tokenize import word_tokenize

def tokenize(corpus):
    tokenized_corpus = {}
    for doc_id, text in corpus.items():
        # Convert text to lowercase before tokenization
        text = text.lower()
        tokenized_corpus[doc_id] = word_tokenize(text)
    return tokenized_corpus