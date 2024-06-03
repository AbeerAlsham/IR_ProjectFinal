from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

lemmatizer = WordNetLemmatizer()

def lemmatize(corpus):
    lemmatize_corpus = {}
    for doc_id, words in corpus.items():
        # Get the POS tag for each word in the document
        pos_tags = pos_tag(words)
        # Lemmatize each word with the appropriate POS tag
        lemmatized_words = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(pos_tag)) for word, pos_tag in pos_tags]
        lemmatize_corpus[doc_id] = lemmatized_words
    return lemmatize_corpus


# Function to convert simple nltk pos tags to wordnet pos tags
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun