import requests
from bs4 import BeautifulSoup

#This function print the top 0-3 results of the user search request from
# website mightyape.co.nz. Results included product title, price, and link 
# for further information
def mighty_results(query):
    search_corrected = query.replace(" ", '%20')
    search_link = "https://www.mightyape.co.nz/search?q=" + search_corrected
    page = requests.get(search_link).text
    soup = BeautifulSoup(page, 'lxml')
    games = soup.findAll('div', class_ = "product")
    count = 0
    print("====== Mighty Ape Results =======")
    if(len(games) == 0):
        print("No results found\n")
    for g in games:
        gme = g.find('div', class_ = "title").text
        dollars = g.find('span', class_ = "dollars").text
        cents = g.find('span', class_ = "cents").text
        link = g.find('a')
        print(gme[1:-1]) #Needs string splicing as website returns with newlines
        print("$" + dollars + cents)
        print("https://www.mightyape.co.nz" + link['href'] +"\n")

        #Below will break the the loop if first 3 products have been printed
        count = count + 1
        if (count >=3):
            break
