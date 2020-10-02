from datetime import datetime
import pytz
import requests
import urllib.request,json

API_KEY = 'c681cd77108c5adeb24293a39d96af72'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'
DEFAULT_TIME = 'Kenya/Nairobi'
TIME_FMT = '%H:%M:%S %Z%z'
# Getting api key
api_key = None
# Getting source url
source_url= None


def configure_request(app):
    global API_KEY, API_URL
    #API_KEY = app.config['WEATHER_API_KEY']
    #API_URL= app.config['WEATHER_API_SOURCE_URL']
    
    FORECAST_API= app.config['FORECAST_API_SOURCE_URL']
    


def get_local_time(utstamp, country, city):
    utc_dt = datetime.utcfromtimestamp(int(utstamp)).replace(tzinfo=pytz.utc)

    timezones = pytz.country_timezones.get(country.upper(), [])
    closest_timezone = [tz for tz in timezones if city.lower() in tz.lower()]

    if closest_timezone:
        tz = closest_timezone[0]  # tz + city
    elif timezones:
        tz = timezones[0]  # just tz
    else:
        tz = DEFAULT_TIME  # emea

    loc_tz = pytz.timezone(tz)
    dt = utc_dt.astimezone(loc_tz)
    return dt.strftime(TIME_FMT)


def query_api(city):

    try:
        #import pdb; pdb.set_trace()
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    #import pdb; pdb.set_trace()
    return data