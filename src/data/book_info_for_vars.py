from pymongo import MongoClient
import pickle
client=MongoClient()
db = client['proj_4_gutenberg']
collection = db['gutenberg_books']

def get_book_info():    
    book_ids = collection.find({}, {'_id':1, 'title':1, 'author':1})
    books_for_dict = {}
    book_nums = []
    book_titles = []
    book_authors = []
    for book in book_ids:
        book_nums.append((book['_id']))
        book_titles.append((book['title']))
        book_authors.append((book['author']))

        url = 'https://www.gutenberg.org/ebooks/%s' % book['_id']
        books_for_dict[book['title']]=[book['author'],url]
    
    return [books_for_dict, book_nums, book_titles, book_authors]

#book_info = get_book_info()
#books_for_dict, book_nums, book_titles, book_authors = (book_info[0],
#                                                        book_info[1],
#                                                        book_info[2],
#                                                        book_info[3])
def update_url_pickle():
    book_info = get_book_info()
    urls = book_info[0]
    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/src/visualization/flask_app/dict_with_urls.pk', 'wb') as write_file:
        pickle.dump(urls, write_file)

def update_title_pickle():
    book_info = get_book_info()
    titles = book_info[2]
    with open('/Users/mbarry/Documents/Coding/ds/metis/projects/gutenberg_recommender/src/visualization/flask_app/book_titles.pk', 'wb') as write_file:
        pickle.dump(titles, write_file)
