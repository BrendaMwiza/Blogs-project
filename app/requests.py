from app import app
import urllib.request,json
from .models import Quotes


# Getting the base url
base_url = app.config["QUOTES_API_BASE_URL"]

def get_quote(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quote_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        results_for = None

        if get_quote_response['results']:
            quotes_lists = get_quote_response['results']
            results_for = process_results(quotes_lists)
    return results_for

def process_results(quote_list):
    '''
    Function  that processes the quotes result and transform them to a list of Objects
    '''
    results_for = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('original_author')
        quote = quote_item.get('quote')
        
        if quote:
            quote_object = Movie(id,author,quote)
            results_for.append(quote_object)

    return results_for
