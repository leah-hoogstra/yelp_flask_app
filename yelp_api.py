from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key = environ["CONSUMER_KEY"] ,            
    consumer_secret = environ["CONSUMER_SECRET"] ,      
    token = environ["TOKEN"] ,                           
    token_secret = environ["TOKEN_SECRET"]             
)

client = Client(auth)

# write a funciton to search for a term on Yelp in a given location 
def get_businesses(term, location):
    params = {
    'term': term,
    'lang': 'en',
    'limit': 3
    }

    response = client.search(location, **params)

    business_list = []

    for business in response.businesses:
        # build a 'wrapper' around the API
        # create our own dictionary of businesses, only inlcuding the information we are interested in
        business_list.append({"name": business.name, 
            "rating": business.rating, 
            "phone": business.display_phone
        })       
    
    return business_list