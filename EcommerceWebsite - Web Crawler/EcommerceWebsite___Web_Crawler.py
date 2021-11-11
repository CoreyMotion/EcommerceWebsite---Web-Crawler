from bs4 import BeautifulSoup
from noelLeeming import noel_results
from theWarehouse import warehouse_results
from mightyApe import mighty_results

# The purpose of this script is to compare products/prices across NZ retail stores
# Websites noelleeming, thewarehouse, and mightape have been scraped and the results
# returned and printed for user to compare.
while(True):
    search_req = input("Enter a game title you'd like to search for:\nq to quit\n")
    if(search_req == 'q'):
        break
    print()
    try:
        noel_results(search_req)
    except:
        print("Problem occured while searching noelleeming")
    try:
        warehouse_results(search_req)
    except:
        print("Problem occured while searching warehouse")
    try:
        mighty_results(search_req)
    except:
        print("Problem occured while searching mighty ape")