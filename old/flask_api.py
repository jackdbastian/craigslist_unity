from flask import Flask
from flask_restful import Resource, Api
from craigslist import CraigslistHousing, CraigslistForSale
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
api = Api(app)

class craigslist_search(Resource):
    def get(self, query):
        results = list(CraigslistForSale(site = 'sfbay', filters={'query': query, 'has_image': True}).get_results(limit = 10))
        for i in results:
            del i['id']
            del i['repost_of']
            del i['has_image']
            del i['last_updated']
            del i['deleted']
            del i['geotag']
            i['image_url'] = BeautifulSoup(requests.get(i['url']).text).select("img")[0]['src']
        return results

api.add_resource(craigslist_search, '/<string:query>')

if __name__ == '__main__':
    app.run(debug=True)
