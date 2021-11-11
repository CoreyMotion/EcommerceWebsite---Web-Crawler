import requests
from bs4 import BeautifulSoup

#This function print the top 0-3 results of the user search request from
# website noelleeming.co.nz. Results included product title, price, and link 
# for further information
def noel_results(query):
    search_corrected = query.replace(" ", '+')
    search_link = "https://www.noelleeming.co.nz/search?q=" + search_corrected
    page = requests.get(search_link).text
    soup = BeautifulSoup(page, 'lxml')
    games = soup.findAll('div', class_ = "product-tile")
    count = 0
    print("====== Noel Leeming Results =======")
    if(len(games) == 0):
        print("No results found\n")
    for g in games:
        gme = g.find('a', class_ = "link text-emphasized").text
        price = g.find('span', class_ = "now-price").text
        link = g.find('a')
        print(gme)
        print(price)
        print("https://www.noelleeming.co.nz" + link['href'] +"\n")

        #Below will break the the loop if first 3 products have been printed
        count = count + 1
        if (count >=3):
            break
