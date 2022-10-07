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
