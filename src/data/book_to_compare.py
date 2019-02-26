from spacy_lemmer import spacy_lem_text
import re



def new_test_book(file_location, title):
	test_book = open(file_location, 'r')
	test_book_title = title
	test_book_string = [line.strip() for line in test_book]
	test_book.close()
	test_book_forlem = ''
	for x in test_book_string:
	    test_book_forlem += x

	if len(test_book_forlem)>50000:
	    test_book_forlem= test_book_forlem[0:50000]

	test_book_forlem = re.sub('[”“]', '', test_book_forlem)
	# remove numbers
	test_book_forlem = re.sub('\w*\d\w*', ' ', test_book_forlem)
	lemmed_test = [spacy_lem_text(test_book_forlem)]

	return lemmed_test

def test_title(title):
	test_book_title = title
	return test_book_title