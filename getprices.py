import requests
from bs4 import BeautifulSoup
import lxml
def getprice(ticker, exchange):
    url = 'https://www.google.com/finance/quote/'+ticker+':'+exchange
    r = requests.get(url)
    soup = BeautifulSoup (r.content, 'lxml')
    price = str((soup.find(class_="YMlKec fxKbKc")))
    return (float((price.replace('<div class="YMlKec fxKbKc">$','').replace('</div>',''))))
#syntaxis:getprice('ticker','exchange')
