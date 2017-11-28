import webbrowser, sys, requests, bs4

page = requests.get("https://coinmarketcap.com/currencies/bitcoin/")

htmldoc = page.content

soup = bs4.BeautifulSoup(htmldoc, 'html.parser')

#print(soup.prettify())

print(soup.find_all("span", class_="text-large"))
#price = tree.xpath('//span[@id="quote_price"]/text()')