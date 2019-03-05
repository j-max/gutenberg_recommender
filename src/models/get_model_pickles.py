from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans

from sklearn.decomposition import TruncatedSVD

import pickle

def update_flask_pickles():
    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/data/processed/spacy_lemmed_new_500000.pickle', 'rb') as read_file:
        lemmed_text = pickle.load(read_file)
    tfidf = TfidfVectorizer()
    doc_word = tfidf.fit_transform(lemmed_text)

    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/src/models/tf_idf.pk', 'wb') as write_file:
        pickle.dump(tfidf, write_file)

    lsa = TruncatedSVD(45)
    doc_topic = lsa.fit_transform(doc_word)
    
    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/src/models/lsa.pk', 'wb') as write_file:
        pickle.dump(lsa, write_file)

    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/src/models/doc_lsa.pk', 'wb') as write_file:
        pickle.dump(doc_topic, write_file)

    
        

