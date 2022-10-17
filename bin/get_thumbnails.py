"""
MIT License

Copyright (c) 2022 Fabian Gabel and Julian Großmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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
        print(f"Downloading https://img.youtube.com/vi/{id}/maxresdefault.jpg ...")
        r = requests.get(url, allow_redirects=True)
        with open(f"{dest}/{nodeId}/{id}.jpg", 'wb') as img:
            img.write(requests.get(url).content)
