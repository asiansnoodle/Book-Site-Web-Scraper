# import all required libraries
import requests
from bs4 import BeautifulSoup

books = {}

# pull content from the url
url = "https://books.toscrape.com/"
r = requests.get(url)
# print(r.content)

soup = BeautifulSoup(r.content, "html5lib")

# print(soup.prettify())

table = soup.find('ol', attrs = {'class': 'row'} )

# print(table.prettify())

for row in table.find_all_next('li', attrs = {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}):
#   print(row.h3.a['title'])
    price = row.find('p', attrs = {'class': 'price_color'})
    title = row.h3.a['title']
    price = float(price.text[1:])
#   print(f"{title}: {price}")
    if (row.h3.a['title']) not in books:
        books[row.h3.a['title']] = price

print(books)