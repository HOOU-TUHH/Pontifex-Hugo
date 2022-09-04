"""Get thumbnails of youtube videos

This script allows the user to create index.json for a given node in graph.json

input:  (1) graph.json
        [(2) dest] optional

output: thumbnails in destination folder

usage: python3 get_thumbnails.py graph.json destination 
"""

import json
import os
import requests
import sys

# read in graph json file
with open(sys.argv[1], 'r') as input:
    mydata = json.load(input)

nodes = mydata["nodes"]

# read in destination
try:
    dest = sys.argv[2]
except IndexError:
    dest = "./"

for node in nodes:
    # extract youtube id and node id
    yt = nodes[node]["video"]
    id = yt[yt.find("embed/")+6:yt.find("?start")]
    nodeId = nodes[node]["id"]
    # if youtube id exists download the thumbnail to corresponding folder
    if (id != ""):
        os.makedirs(os.path.join(dest,nodeId), exist_ok=True)
        url = f"https://img.youtube.com/vi/{id}/maxresdefault.jpg"
        r = requests.get(url, allow_redirects=True)
        with open(f"{dest}/{nodeId}/{id}.jpg", 'wb') as img:
            img.write(requests.get(url).content)
