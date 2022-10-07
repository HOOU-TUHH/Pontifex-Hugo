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

"""Build xxx.json

This script allows the user to create index.json for a given node in graph.json

input:  (1) graph.json
        (2) index as number

output: index.json in console

usage: python3 makejson.py graph.json index > index/index.json
"""

import json
import sys

## function: input: json, id ,  output: json in console print(json)

import logging


with open(sys.argv[1], 'r') as input:
 mydata = json.load(input)

index = str(sys.argv[2])

nodes = mydata["nodes"]
edges = mydata["edges"]

# Check if index is in nodes
try:
  mynode = nodes[index]
except:
  logging.critical(f"The Node number {index} is missing in graph.json!")
  sys.exit(1)

def add_edge_attributes(edge):
  y = edge["target"]
  if y == index:
    edge["color"] = "#abe8ef"
    edge["style"] = "solid"
  else:
    edge["color"] = "#b8b8b8"
    edge["style"] = "dashed"

def all_connections(node):
  node_id = node["id"]
  connections = []
  real_nodes = [{"data": node}]
  # the order matters for the visualization 
  # (group incoming and outgoing nodes)
  for edge in edges.values():
    if edge["source"] == node_id:
      real_nodes.append(dict({"data": nodes[edge["target"]]}))
      nodes[edge["target"]]["color"] = "#b8b8b8"
      add_edge_attributes(edge)
      connections.append({"data":edge})

  for edge in edges.values():
    if edge["target"] == node_id:
      real_nodes.append(dict({"data": nodes[edge["source"]]}))
      nodes[edge["source"]]["color"] = "#abe8ef"
      add_edge_attributes(edge)
      connections.append({"data":edge})

  return connections, real_nodes

real_edges, real_nodes = all_connections(mynode)

mydata2 = dict()
mydata2["nodes"] = real_nodes
mydata2["edges"] = real_edges

# the json file where the output must be stored 
pretty_obj = json.dumps(mydata2, indent = 6)
print(pretty_obj)
