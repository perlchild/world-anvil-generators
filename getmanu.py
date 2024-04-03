import os
from pprint import pprint
import requests
from dotenv import *

load_dotenv(".env/nonprod.env")  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
headers = dict(filter(lambda item: item[0].lower() in ['url','url_man','url_man2', 'x-application-key', 'x-auth-token','user-agent','content-type'], os.environ.items()))
# if i[0] == "X":
#     print(i, j)
print(headers)
list_of_worlds=[]
with  requests.post(headers['URL']+"?id=ab2dd14a-f027-4ff3-a9c9-0724ccbded65", headers=headers) as r:
    try:
        print( r.status_code)
        for entities in r.json()['entities']:
            list_of_worlds.append(entities['id'])
    except e:
        print(e)
for id in list_of_worlds:
    list_of_manuscripts = []
    try:
        #print(headers['URL_MAN'] + '?id=' + id)
        with requests.post(headers['URL_MAN']+"?id="+id, headers=headers) as r:
            print(r.status_code)
            #pprint(r.json())
            print()
            for entities in r.json()['entities']:
                list_of_manuscripts.append(entities['id'])
    except e:
        print(e)
    for id in list_of_manuscripts:
        print(headers['URL_MAN2'] + '?id=' + id)
        try:
            with requests.get(headers['URL_MAN2']+'?id='+id, headers=headers ) as r:
                pprint(r.json())
        except e:
            print(r.status_code)
            print (e)
