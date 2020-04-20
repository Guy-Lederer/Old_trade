import requests
from bs4 import BeautifulSoup
import re
import time

url1 = input('Enter the stock url:')

#url2 = input('Enter the stock url:')

#url1 = "https://il.investing.com/equities/facebook-inc"

url2 = "https://il.investing.com/equities/google-inc"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36"
}

req = requests.Session()
try:
    res1 = req.get(url1, headers=headers)
    res2 = req.get(url2, headers=headers)
except:
    print("The URL is not valid")


def get_stock_price_index(res):
    soup = BeautifulSoup(res.text, features='html.parser')
    # finding price
    price = soup.find(id='last_last').get_text()
    # removing comma and rupee sign we will be using regex
    price = float(re.sub(',', '', price))
    title = soup.find(class_="float_lang_base_1 relativeAttr").get_text()
    title = title.strip()
    print('Stock:', title)

    max_price = float(input("Enter the maximum stock price index you want the stock to be in:"))
    if price < max_price:
        print("Buy it the stock is low: -->", price)
    else:
        print(f"Price still high --> {price}")


while True:
    get_stock_price_index(res1)
    get_stock_price_index(res2)
    #time.sleep(10)
