from nltk.corpus import stopwords

# NLTK English stopwords
stopwords_list = stopwords.words('english')

# Additional common English contractions
contractions = ["''", "``", "..", "n't", "'s", "u", "'m", "’", "'", "/", "...", ".", "”", "””", "wa", "hi", "doe", "ha", "whi"]

# Some common words that often appear in text but may not carry much meaning
common_words = ['get', 'got', 'hey', 'hmm', 'hoo', 'let', 'ooo', 'par', 'pdt', 'pln', 'pst', 'wha', 'yep', 'yer', 'aest', 'didn', 'nzdt', 'via', 'one', 'com', 'new', 'like', 'great', 'make', 'top', 'awesome', 'best', 'good', 'wow', 'yes', 'say', 'yay', 'would', 'thanks', 'thank', 'use', 'should', 'see', 'want', 'nice', 'while', 'know']

# Combine the lists
stopwords_list += contractions + common_words

# Convert to a set for faster lookup
stopwords_set = set(stopwords_list)


def remove_stopwords(corpus):
    stopwords_corpus = {}
    for doc_id, words in corpus.items():
        stopwords_corpus[doc_id] = [word for word in words if word not in stopwords_set]
    return stopwords_corpus
    