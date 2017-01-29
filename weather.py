import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# os.environ["FORECASTIO_KEY"] 

# create a function which returns the weather info for you given specific address
def get_weather(address):
	# call up the current forecast. 
	api_key = os.environ['FORECASTIO_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	lat_long = [location.latitude, location.longitude]
	forecast = forecastio.load_forecast(api_key, lat_long[0], lat_long[1]).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° in {}".format(summary, temperature, address)
