import urllib
import json
import requests

url_endpoint = 'http://write_event:7000/events'

def write_event(arg1,arg2):
#def read_event(request_parapms):
    body = {
    'pod_id':arg1,
    'msg':arg2
    }

    #content = requests.get(url=url_endpoint, params = request_parapms)
    newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #content = requests.post(url=url_endpoint, data = body,headers=newHeaders)
    content = requests.post(url=url_endpoint, json = body)
    #content = requests.get(url=url_endpoint)
    print('response from write-tire: ', content.status_code)
    return str(content.status_code)
    #return jsonify({'message': string, 'random' : json.loads(content)['message']})
