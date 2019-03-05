import pickle
from pymongo import MongoClient

import sys
sys.path.insert(0, '../src/features/')
sys.path.insert(0, '../../../src/data/')

from book_info_for_vars import get_book_info
book_info = get_book_info()
book_nums = book_info[1]
print(book_nums)
with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/data/processed/spacy_lemmed_new_500000.pickle', 'rb') as read_file:
    lemmed_text = pickle.load(read_file)

def get_lem_dict():
    lemmed_dict = {}

    for _id, text in zip(book_nums, lemmed_text):
        lemmed_dict[_id] = text

    return lemmed_dict

def update_lem_dict():
    lemmed_dict = get_lem_dict()
    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/src/visualization/flask_app/dict_with_lems.pk', 'wb') as write_file:
        pickle.dump(lemmed_dict, write_file)
