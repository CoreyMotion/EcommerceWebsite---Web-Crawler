import requests
from bs4 import BeautifulSoup

#This function print the top 0-3 results of the user search request from
# website thewarehouse.co.nz. Results included product title, price, and link 
# for further information
def warehouse_results(query):
    search_corrected = query.replace(" ", '+')
    search_link = "https://www.thewarehouse.co.nz/search?q=" + search_corrected
    page = requests.get(search_link).text
    soup = BeautifulSoup(page, 'lxml')
    games = soup.findAll('div', class_ = "product-tile")
    print("====== The Warehouse Results =======")
    count = 0
    if(len(games) == 0):
        print("No results found\n")
    for g in games:
        gme = g.find('a', class_ = "link text-emphasized").text
        price = g.find('span', class_ = "now-price").text
        link = g.find('a')
        print(gme)
        print(price)
        print("https://www.thewarehouse.co.nz" + link['href'] +"\n")

        #Below will break the the loop if first 3 products have been printed
        count = count + 1
        if (count >=3):
            break
