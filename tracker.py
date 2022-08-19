import requests
from bs4 import BeautifulSoup
from email_alert import alert_system
from threading import Timer

"""n = input("Enter number of stocks: ")

stocks = []
my_price = []
i = 0
for i in range((int(n))):
    stocks.append( input("enter URL: ") )  
    my_price.append( input("enter URL: ") )"""
    
#for i in range((int(n))):

URL = input("Enter URL: ")
#URL = "https://www.google.com/search?q=tata+consumer+share+price+nse&oq=tata&aqs=chrome.1.69i57j69i59l3j35i39i285j0i67i131i433l3j46i67i199i291j46i131i199i291i433i512.1535j0j1&sourceid=chrome&ie=UTF-8"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

price = input("Enter desired price: ")
set_price = int(price)

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(class_ ="yKMVIe").get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    price = soup.find(class_ ="IsqQVc NprOob wT3VGc").get_text()
    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) <= set_price:
        alert_system(product_title, URL)
        print("sent")
        return
    else:
        print("not sent")
    Timer(60, check_price).start()

check_price()