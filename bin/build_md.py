"""Make Markdown File 

This script allows the user to put everything into a md-file for hugo
Requires JSON file from prior run of build_json.py 

input:  (1) index = xxx

output: xxx.md

usage: python3 make_md.py xxx
"""

import json
import sys
import re
from collections import defaultdict

index = str(sys.argv[1])
path = f"{index}/{index}"

with open(f"{path}.json", 'r') as input:
    mydata = json.load(input)

nodes = mydata["nodes"]
edges = mydata["edges"]

mylines = []                                # Declare an empty list.
with open(f"../nodes/dummy_for_hugo.md", 'rt') as myfile:  # open file
    for myline in myfile:                   # For each line in the file,
        mylines.append(myline.rstrip('\n'))

# Read graph database
with open('../nodes/graph.json', 'r') as f:
    mydata = json.load(f)

mynode = defaultdict(str,mydata["nodes"][index])

# preprocess youtube
def get_youtubeid(link):
    # regex based on https://stackoverflow.com/a/34833500/
    pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
    youtubeid = re.search(pattern, link, re.IGNORECASE)
    if youtubeid is None:
        return ""
    else:
        return youtubeid.group(1)

def get_youtubetime(link):
    youtubetime =  re.search(r'start=[0-9]*', link, re.IGNORECASE)
    if youtubetime is None:
        return ""
    else:
        return youtubetime.group(0)

# read content from json file
filename = mynode["notes"]
webworklink = mynode["webwork"]
exerciselink = mynode["exercise"]
title = mynode["label"].replace('\n',' ')
content = mynode["content"]
podcast = mynode["podcast"]
timestamp = "2022-04-01T08:48:57+00:00"
chapter = f"chapter{index[0]}"

## WeBWorK
webworkstring = f"""## Solve the WeBWorK exercise\n {{{{< webwork "{webworklink}">}}}}""" if webworklink != "" else ""

## Exercise
exercisestring = f"""## Solve the Exercise\n {{{{< webwork "{exerciselink}">}}}}""" if exerciselink != "" else ""

## youtube and video
video = mynode["video"]
youtubelink = mynode["youtube"]
youtubeid = get_youtubeid(youtubelink)
youtubetime = get_youtubetime(youtubelink)
youtubend = youtubeid + "?" + youtubetime

ntabs = 2
# preprocess video / youtube
if video != "":
    ntabs = ntabs + 1
    video = '{{< tab tabName="Video">}}\n'+  video +  '\n{{< /tab >}}\n'
elif youtubelink != "":
    ntabs = ntabs + 1
    video = '{{< tab tabName="Video">}}\n' + f'Click [here](https://youtu.be/{youtubeid}) or on the thumbnail below to open up the YouTube video in a separate tab!  <a href="https://youtu.be/{youtubeid}?{youtubetime}" target="_blank"> <img src="./{youtubeid}.jpg"></a>' + '\n{{< /tab >}}\n'

# preprocess podcast
if podcast != "":
    ntabs = ntabs + 1
    podcast = '{{< tab tabName="Podcast">}}\n'+  podcast +  '\n{{< /tab >}}\n'

# read notes with spaces in front of each line
mynotes = ""
with open(f"../nodes/{index}/{filename}", 'rt') as myfile2:
    for myline in myfile2:
        mynotes = mynotes + myline

#predecessors and successors
def match_edge(nid):
    """checks if edge has source or target as given id"""
    for edge in edges:
        if edge["data"]["source"] == nid:
            return "s"
        if edge["data"]["target"] == nid:
            return "t"

def snippet(a, b, c=0):
    """takes input to put it into table form"""
    if c == 1:
        c = ' class="bg-danger"'
    else:
        c = ''
    string = f"""
<tr{c}>
<th scope="row">{a}</th>
<td>{b}</td>
</tr>
        """
    return string

def read_node(node):
    """gives id, label with link and content of a node"""
    nid = node["data"]["id"]
    cid = f"chapter{nid[0]}"
    a = node["data"]["label"]
    b = node["data"]["content"]
    a = f'<a href="../../{cid}/{nid}/">{a}</a>'
    return (nid, a, b)

mystring = ""
mystring2 = ""

# Equal index
for node in nodes:
    (nid, a, b) = read_node(node)
    if nid == index:
        # mystring2 += snippet(a, b, 1) # Don't add current node
        # change headertag
        for ind, myline in enumerate(mylines):
            new = f"""Topic: <a href="{index}-node.html">{node["data"]["label"]}</a>"""
            if f'<h1 id="headertag">NODE {index}</h1>' in myline:
                mylines[ind] = f'      <h1 id="headertag">{new}</h1>'

# Unequal index
for node in nodes:
    (nid, a, b) = read_node(node)
    if nid != index:
        if match_edge(nid) == "s":
            mystring += snippet(a, b)
        elif match_edge(nid) == "t":
            mystring2 += snippet(a, b)

preds = mystring
succs = mystring2

# define fillers
fillers = ["###TITLE###", "###DEC###", "###TIME###", "###CHAP###","###INDEX###", "###TABLEPRED###", "###TABLESUCC###", "###NOTES###", "###YTURLEND###","###YTID###", "###PODCAST###", '###VIDEO###', "###WEBWORK###", "###EXERCISE###", "###NTABS###"]

# put content into same order
content = [title, content, timestamp, chapter, index, preds, succs,mynotes, youtubend, youtubeid, podcast, video, webworkstring, exercisestring, str(ntabs)]


for ind, myline in enumerate(mylines):
    for num, filler in enumerate(fillers):
        if filler in myline:
            mylines[ind] = myline.replace(filler, content[num])

# Write HTML
with open(f"{index}.md", "w") as file:
    for element in mylines:                     # For each element in the list,
        file.write(element+"\n")
