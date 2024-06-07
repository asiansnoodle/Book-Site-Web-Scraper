# import all required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

books = {}

def scrapePage(url):
    r = requests.get(url)
    # print(r.content)
    soup = BeautifulSoup(r.content, "html5lib")
    # print(soup.prettify())
    table = soup.find('ol', attrs = {'class': 'row'} )
    # print(table.prettify())

    if table is None:
        newBase = "https://books.toscrape.com/catalogue/"
        newURL = newBase + url[27:]

        r = requests.get(newURL)
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('ol', attrs= {'class': 'row'})

    for row in table.find_all_next('li', attrs = {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}):
    #   print(row.h3.a['title'])
        price = row.find('p', attrs = {'class': 'price_color'})
        title = row.h3.a['title']
        price = float(price.text[1:])
    #   print(f"{title}: {price}")
        if (row.h3.a['title']) not in books:
            books[title] = price

# pull base URL
baseURL = "https://books.toscrape.com/"

# initialize a current url to track with page we're on
currentURL = baseURL

# loop to scrape each page
while True:
    scrapePage(currentURL)

        # Locate the 'Next' button on the page
    r = requests.get(currentURL)
    soup = BeautifulSoup(r.content, "html5lib")
    nextButton = soup.find('li', attrs = {'class': 'next'})
    if nextButton is None:
        newBase = "https://books.toscrape.com/catalogue/"
        newURL = newBase + currentURL[27:]

        r = requests.get(newURL)
        soup = BeautifulSoup(r.content, 'html5lib')
        nextButton = soup.find('li', attrs = {'class': 'next'})
    

    if nextButton:
        currentURL = baseURL + nextButton.a['href']
    else:
        break

df = pd.DataFrame(list(books.items()), columns=['title', 'price'])

df.to_csv('books.csv')
