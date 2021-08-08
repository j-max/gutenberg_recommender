import time
from bs4 import BeautifulSoup
import requests
import os
import re

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

'''
testing text scrape with Jane Austin (1st book of top 100)
'''
jane_austin = requests.get(top_10_urls[0])
austin_soup = BeautifulSoup(jane_austin.content)

# first table contains all the download options
austin_table = austin_soup.find('table')
rows = austin_table.find_all('tr')
ebook_url = rows[1]

if "Read this book online" in ebook_url.text:
    print("Ebook found")

pride_url = ebook_url['about']
pride_response = requests.get(austin_url)
pride_html = BeautifulSoup(pride_response.text)

''' The text of the book is held in the p tags.
This can be confirmed by seeing that the first and last
p tags align with the first and last sentence of the book'''

pride_text = pride_html.find_all('p')
print(f'There are {len(pride_text)} paragraphs in Pride and Prejudice')

# test on a multi sentence paragraph
# Thanks to this SO https://stackoverflow.com/questions/3549075/regex-to-find-all-sentences-of-text
# for the regex pattern
strip_sent = pride_text[-1].text.replace('\r\n', '')
strip_sent = strip_sent.replace('\n','')
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
sent = pat.findall(strip_sent)
