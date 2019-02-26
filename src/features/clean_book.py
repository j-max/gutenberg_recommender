import re
from pymongo import MongoClient


client=MongoClient()
db = client['proj_4_gutenberg']
collection = db['gutenberg_books']

def book_cleaner(book_id):
    '''Finds book in mongo data base and returns a book without
    punctuation, numbers, and capital letters.'''

    book = collection.find({'_id': str(book_id)}, {'_id': 1, 'title': 1, 'author': 1, 'text': 1})
    book_text = []
    book_title = ''
    for x in book:
        book_text = x['text']
        book_title = x['title']
#     if len(book_text)>999999:
#         book_text = book_text[:999999]
    if len(book_text)>50000:
        #beginning at 1000 to manually cut out the chapter words.
        book_text = book_text[1000:500000]
    clean_book = re.sub('[”“]', '', book_text)
    # remove numbers
    clean_book = re.sub('\w*\d\w*', ' ', clean_book)
    clean_book = re.sub('[cC][hH][aA][pP][tT][eE][rR]', ' ', clean_book)
    print(book_title, len(book_text))
    return clean_book
