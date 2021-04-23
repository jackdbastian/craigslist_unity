from craigslist import CraigslistHousing, CraigslistForSale
from bs4 import BeautifulSoup
import requests
import json

def cut_out(results):
    for i in results:
                # del i['id']
                del i['repost_of']
                del i['has_image']
                del i['last_updated']
                # del i['deleted']
                del i['geotag']
                i['image_url'] = BeautifulSoup(requests.get(i['url']).text).select("img")[0]['src']

beaters = list(CraigslistForSale(
    site='sfbay',
    category='cta', 
    filters={
        'has_image': True,
        'max_year': 1980,
        'max_price': 1000}
).get_results(limit = 10))

cut_out(beaters)

hot_rods = list(CraigslistForSale(
    site='sfbay',
    category='cta', 
    filters={
        'has_image': True,
        'min_year': 1990,
        'max_year': 2000,
        'min_price': 8000}
).get_results(limit = 10))

cut_out(hot_rods)

cheap_toys = list(CraigslistForSale(
    site='sfbay',
    category='taa', 
    filters={
        'has_image': True,
        'max_price': 5}
).get_results(limit = 10))

cut_out(cheap_toys)

expensive_toys = list(CraigslistForSale(
    site='sfbay',
    category='taa', 
    filters={
        'has_image': True,
        'min_price': 50}
).get_results(limit = 10))

cut_out(expensive_toys)

craig_dict = {
    "cars": {
        "beaters": beaters,
        "hot rods": hot_rods
    },
    "toys": {
        "cheap toys": cheap_toys,
        "expensive toys": expensive_toys
    }
}

j = json.dumps(craig_dict, indent=4)
f = open('/Users/Jack/Documents/GitHub/craigslist_unity/data/sfbay.json', 'w')
print(j, file=f) 
f.close()
