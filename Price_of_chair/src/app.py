import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-brooks-side-dining-chairs-set-of-2/antique-brown/p3189169")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "u-centred price"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)
print(price)
if price < 200:
    print("You should buy the chair")
    print("The current price is {}.".format(string_price))
else:
    print("Do not buy chair, it is Expensive!")