gutenberg_recommender
==============================

> The goal of this project is to use natural language processing to make [Project Gutenberg](https://www.gutenberg.org/) reading recommendations.  Project Gutenberg is an online source of free eBooks. The end product is a Flask app which allows a user to submit a snippet of text and recieve three texts that they might enjoy reading for free on Project Gutenberg. 

Data
==============================
The data for this project includes a selection of the Top 100 books read on Project Gutenberg as tracked in February 2019.  The text of these books were scraped from the site using Selenium (at a respectful ping rate) and beautiful soup. The raw book text was then stored in a Mongo database. See [here](notebooks/Gut_scrape.ipynb) for the associated code.

Text Preparation
==============================

I use Spacy to tag the text with part of speech and [lemmatize](./src/features/spacy_lemmer.py). I cut out the first 1000 words of each text to remove the Project Gutenberg metadata, and then select the first 500000 characters from the book for preparation [here](src/features/clean_book.py). Once the texts have been cleaned (stopwords removed, punctuation removed, made lowercase), I feed them into a TFIDF vectorizor which ignores infrequent (<10%) and frequent (>80%) and includes bigrams. Look in [here](notebooks/gutenberg_proj4_notebook.ipynb) for TFIDF vectorization.

Modeling and Flask App
==============================
I employ LSA and NMF clustering to the tfidf vectorized texts.  The results can be seen towards the end of [this notebook](notebooks/gutenberg_notebook.ipynb). I then store the strength of expression of each document topic so it can be used to find the top 3 most similar books using cosine similarity. <br>
The [flask app](src/visualization/flask_app/main.py) takes in a snippet of a book from the user, then uses the [cosine_recommender](src/visualization/flask_app/main.py) function to return the 3 most similar books.
