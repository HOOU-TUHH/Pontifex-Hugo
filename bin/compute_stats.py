"""Compute stats of graph

Count nodes, edges and podcast episodes

input:  (1) graph.json

output: Table in console and svgs to embed on webpage

usage: python3 compute_stats.py graph.json 
"""

import json
import sys
import anybadge

with open(sys.argv[1], 'r') as input:
 mydata = json.load(input)

nodes = mydata["nodes"]
edges = mydata["edges"]

# Count non-empty podcasts entries
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
