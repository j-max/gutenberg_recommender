import time
from bs4 import BeautifulSoup
import requests
import os

'''
On August 5th, 2021, the top 8 most popular eBooks are good candidates for the project: From Pride and Prejudice to Frankenstein.
'''

top_books_url = 'https://www.gutenberg.org/browse/scores/top'
response = requests.get(top_books_url)
soup = BeautifulSoup(response.content)

# the first ordered list on this page is the top 100 books from yesterday
top_100 = soup.find('ol')
top_100 = top_100.find_all('li')

top_10 = top_100[:10]

# href is the book url embedded in a link
top_10 = {book.text: 'https://www.gutenberg.org' + book.find('a')['href'] for book in top_10}
top_10_urls = list(top_10.values())

jane_austin = requests.get(top_10_urls[0])
austin_soup = BeautifulSoup(jane_austin.content)

# first table contains all the download options
austin_table = austin_soup.find('table')
rows = austin_table.find_all('tr')
ebook_url = rows[1]

if "Read this book online" in ebook_url.text:
    print("Ebook found")
