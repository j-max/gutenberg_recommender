import spacy


def spacy_lem_text(clean_book):
    '''uses spacy to create a lemmatized version 
    of a text to feed into tf-idf.
    
    Parameter: a preprocessed Project Gutenberg book with certain 
    key stop words removed and shortened to 500000 words or less.
    
    Returns: A lemmatized version of the text ready for vectorization.
    '''
    nlp = spacy.load('en_core_web_sm')
    # Spacy takes the raw text and adds POS and Lemma attributes to each token.
    spacy_book = nlp(clean_book)
    book_lem = ''
    for token in spacy_book:
        # Remove proper nouns, as they are not semantically important to this model
        if token.tag_ == 'NNP':
            x=0
        else:
            if token.tag_ != 'NNP' and token.lemma_ != '-PRON-':
                book_lem += ' %s' % token.lemma_
    print(len(book_lem))
    return book_lem

####################
