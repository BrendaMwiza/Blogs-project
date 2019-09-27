# from app import app
import urllib.request,json
from .models import Quotes


api_key = None
# Getting the base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['QUOTE_API_KEY']
    base_url = app.config['QUOTES_API_BASE_URL']


def get_quote(category):
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        results_for = None

        if get_quote_response:
            quotes_lists = get_quote_response
            id = quotes_lists.get('id')
            author = quotes_lists.get('original_author')
            quote = quotes_lists.get('quote')
            results_for = Quotes(id,author,quote)

            
        return results_for


