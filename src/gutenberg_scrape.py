from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
top_100 = soup.select('h2#books-last1')


# chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
# os.environ["webdriver.chrome.driver"] = chromedriver
# 
# driver = webdriver.Chrome(chromedriver)
# 
# driver.get('https://www.gutenberg.org/browse/scores/top')
# 
# '''
# On August 5th, 2021, the top 8 most popular eBooks are good candidates for the project: From Pride and Prejudice to Frankenstein.
# '''
# 
# 
# time.sleep(2)
# driver.close()
