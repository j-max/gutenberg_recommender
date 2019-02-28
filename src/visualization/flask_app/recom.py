import sys
import pickle
import numpy as np 
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

sys.path.insert(0, '../../features/')
sys.path.insert(0, '../../data/')
sys.path.insert(0, '../../models/')
from spacy_lemmer import spacy_lem_text
from clean_book import sample_cleaner

##################pickle imports##################
with open('../../models/tf_idf.pk', 'rb') as read_file:
	tf_idf = pickle.load(read_file)

with open('../../models/lsa.pk', 'rb') as read_file:
	lsa = pickle.load(read_file)

with open('../../models/doc_lsa.pk', 'rb') as read_file:
	doc_topic = pickle.load(read_file)


with open('book_titles.pk', 'rb') as read_file:
	book_titles = pickle.load(read_file)

#################apps for flask###################

def recommender(text_from_form):
	clean_book = sample_cleaner(text_from_form)
	lemmed_book = spacy_lem_text(clean_book)
	tf_idf_sample = tf_idf.transform([lemmed_book])
	lsa_sample = lsa.transform(tf_idf_sample)

	doc_for_k = np.concatenate([doc_topic, lsa_sample], axis=0)
	
	num_clusters = 15
	km = KMeans(n_clusters=num_clusters,random_state=10,n_init=1)
	km.fit(doc_for_k)
	test_title = 'test_title'
	book_titles.append(test_title)

	group_labels = km.labels_
	test_group = ''
	match_group = []
	for group,title in zip(group_labels, book_titles):
	    if title == test_title:
	        test_group = group
	for group,title in zip(group_labels, book_titles):
	    if group == test_group:
	    	if title != test_group:
	        	match_group.append('%s%s' %(title, group))
	return match_group

def cosine_recommender(text_from_form):

	clean_book = sample_cleaner(text_from_form)
	lemmed_book = spacy_lem_text(clean_book)
	tf_idf_sample = tf_idf.transform([lemmed_book])
	lsa_sample = lsa.transform(tf_idf_sample)
	doc_for_k = np.concatenate([doc_topic, lsa_sample], axis=0)

	a= cosine_similarity(doc_for_k)

	top_cos_sim = np.argsort(a[-1])[:-1]
	return ([book_titles[top_cos_sim[-1]], book_titles[top_cos_sim[-2]], book_titles[top_cos_sim[-3]]])
	
