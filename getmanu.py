import os
from pprint import pprint

import requests
from dotenv import *

load_dotenv(".env/nonprod.env")  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
headers = dict(filter(
    lambda item: item[0].lower() in ['url', 'url_man', 'url_man2', 'url_man3', 'url_man4', 'x-application-key',
                                     'x-auth-token', 'user-agent',
                                     'content-type'], os.environ.items()))
# if i[0] == "X":
#     print(i, j)
#print(headers)
world_count = manu_count = version_count = part_count = 0
world_iter = manu_iter = version_iter = part_iter = 0
list_of_worlds = list_of_manuscripts = list_of_manuscript_versions = list_of_manuscript_parts = []

try:
    with requests.post(headers['URL'] + "?id=ab2dd14a-f027-4ff3-a9c9-0724ccbded65", headers=headers) as w:
        w.raise_for_status()
        if 'entities' in w.json():
            for entities in w.json()['entities']:
                list_of_worlds.append(entities['id'])
                world_count += 1

except e:
    print(e)

for world_id in set(list_of_worlds):
    print(f"{headers['URL_MAN']}?id={world_id} : world_id:{world_iter}|{world_count}")
    world_iter += 1
    try:
        with requests.post(headers['URL_MAN'] + "?id=" + world_id, headers=headers) as m:
            #m.raise_for_status()
            with open(world_id + '.json', 'wb') as f:
                for chunk in m.iter_content(chunk_size=8192):
                    f.write(chunk)
            if 'entities' in m.json():
                for entities in m.json()['entities']:
                    list_of_manuscripts.append(entities['id'])
                    manu_count += 1
    except e:
        print(e)
for manu_id in set(list_of_manuscripts):
    print(f"{headers['URL_MAN2']}?id={manu_id} : manu_id:{manu_iter}|{manu_count}")
    manu_iter += 1
    try:
        with requests.get(headers['URL_MAN2'] + '?id=' + manu_id, headers=headers) as v:
            #v.raise_for_status()
            with open(manu_id + '.json', 'wb') as f:
                for chunk in v.iter_content(chunk_size=8192):
                    f.write(chunk)
            if 'entities' in v.json():
                for entities in v.json()['entities']:
                    list_of_manuscript_versions.append(entities['id'])
                    version_count += 1
    except e:
        print(e)
for version_id in set(list_of_manuscript_versions):
    print(f"{headers['URL_MAN3']}?id={version_id} : version_id:{version_iter}|{version_count}")
    version_iter += 1
#     try:
#         with requests.get(headers['URL_MAN3'] + '?id=' + version_id, headers=headers) as p:
#             #p.raise_for_status()
#             if 'entities' in p.json():
#                 for entities in p.json()['entities']:
#                     list_of_manuscript_parts.append(entities['id'])
#                     part_count += 1
#             with open(version_id + '.Vjson', 'wb') as f:
#                 for chunk in p.iter_content(chunk_size=8192):
#                     f.write(chunk)
#             pprint(p.json())
#     except e:
#         print(e)
# for part_id in set(list_of_manuscript_parts):
#     pert_iter += 1
#     print(f"{headers['URL_MAN4']}id={part_id} : part_id|{part_iter}|{part_count}")
#     try:
#         with requests.get(headers['URL_MAN4'] + '?id=' + part_id, headers=headers) as x:
#             #x.raise_for_status()
#             with open(part_id + '.json', 'wb') as f:
#                 for chunk in x.iter_content(chunk_size=8192):
#                     f.write(chunk)
#             pprint(x.json())
#     except e:
#         print(e)
