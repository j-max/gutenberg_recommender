
from spacy.lemmatizer import Lemmatizer
from clean_book import book_cleaner
import spacy


def spacy_lem_text(clean_book):
    '''uses spacy to create a lemmatized version of a text to feed into tf-idf.'''
    nlp = spacy.load('en')
    spacy_book = nlp(clean_book)
    book_lem = ''
    for token in spacy_book:
        if token.tag_ == 'NNP':
            x=0
        else:
            if token.tag_ != 'NNP' and token.lemma_ != '-PRON-':
                book_lem += ' %s' % token.lemma_
    print(len(book_lem))
    return book_lem

####################
