"""Make xxx.json

Count nodes, edges and podcast episodes

input:  (1) cyto.json

output: index.json in console

usage: python3 compute_stats.py cyto.json 
"""

import json
import sys
import anybadge

## function: input: json, id ,  output: json in console print(json)

import logging

with open(sys.argv[1], 'r') as input:
 mydata = json.load(input)

nodes = mydata["nodes"]
edges = mydata["edges"]

# parse such that inline graph definition works
output = []
n_podcasts = 0
for node in nodes:
    if nodes[node]["podcast"] != '':
        n_podcasts += 1

print(f"# Nodes:            {len(nodes)}")
print(f"# Edges:            {len(edges)}")
print(f"# Podcast Episodes: {n_podcasts}")

badge = anybadge.Badge(label='Nodes', value=f'{len(nodes)}')
badge.write_badge('nodes.svg', overwrite=True)

badge = anybadge.Badge(label='Edges', value=f'{len(edges)}')
badge.write_badge('edges.svg', overwrite=True)

badge = anybadge.Badge(label='Podcast Episodes', value=f'{n_podcasts}')
badge.write_badge('podcasts.svg', overwrite=True)