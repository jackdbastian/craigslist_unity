from craigslist import CraigslistHousing, CraigslistForSale
from bs4 import BeautifulSoup
import requests
import json
from random import random

def get_posts(cat, query):
    results = list(CraigslistForSale(
        site='sfbay',
        category=cat, 
        filters={'query': query, 'has_image': True}
    ).get_results(limit = 3))

    for i in results:
        del i['repost_of']
        del i['has_image']
        del i['last_updated']
        del i['geotag']
        i['image_url'] = BeautifulSoup(requests.get(i['url']).text, features="html.parser").select("img")[0]['src']
        i['query'] = query
        i['category'] = cat
    
    return results


# Materials
gravel = get_posts(cat='maa', query='gravel')
wood = get_posts(cat='maa', query='wood')

# Clothes
vintage = get_posts(cat='cla', query='vintage')
beaded = get_posts(cat='cla', query='beaded')
gloves = get_posts(cat='cla', query='gloves')
wedding_dress = get_posts(cat='cla', query='wedding dress')
great_condition = get_posts(cat='cla', query='great condition')

# Assembiling JSON
craig_dict = {
    "materials": {
        "gravel": gravel,
        "wood": wood
    },
    "clothes": {
        "vintage": vintage,
        "beaded": beaded,
        "gloves": gloves,
        "wedding dress": wedding_dress,
        "great condition": great_condition
    }
}

# Exporting JSON
j = json.dumps(craig_dict, indent=4)
f = open('/Users/Jack/Documents/GitHub/craigslist_unity/data/sfbay_v2.json', 'w')
print(j, file=f) 
f.close()
