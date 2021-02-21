import urllib
import json
import requests

url_endpoint = 'http://read_event:6000/events'

def read_event(arg1,arg2):
#def read_event(request_parapms):
    params1 = {
    'sDateTime':arg1,
    'eDateTime':arg2
    }

    #content = requests.get(url=url_endpoint, params = request_parapms)
    content = requests.get(url=url_endpoint, params = params1)
    #content = requests.get(url=url_endpoint)
    print('response from read-tire: ', content.json())
    return str(content.json())
    #return jsonify({'message': string, 'random' : json.loads(content)['message']})
