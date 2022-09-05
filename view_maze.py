import networkx as nx
from random import seed, random
import os
import pickle
import matplotlib.pyplot as plt

import util
from Keys import C, W

# SIZES = [10, 25, 50, 75, 100, 125, 150, 175, 200]
MAZES = 10
GRID_SIZE = 50
SIZE = GRID_SIZE**2
START = (0,GRID_SIZE-1)
END = (GRID_SIZE-1,0)

if not os.path.exists('mazes'):
    os.mkdir('mazes')

SEED = 0

base_path = os.path.join('mazes', f'{SEED}_{GRID_SIZE}')

with open(os.path.join(base_path, 'maze_graph.pkl'), 'rb') as f:
    G = pickle.load(f)

with open(os.path.join(base_path, 'maze_hyper_graph.pkl'), 'rb') as f:
    HG = pickle.load(f)

with open(os.path.join(base_path, 'node_lookup.pkl'), 'rb') as f:
    node_lookup = pickle.load(f)

T = nx.minimum_spanning_tree(G) # turn into maze

path = nx.astar_path(HG, node_lookup[START], node_lookup[END])


# for u,v in T.edges:
#     T[u][v][C] = 'WHITE'

# src = path[0]
# for tgt in path[1:]:
#     T.edges[(src,tgt)][C] = 'RED'
#     src = tgt

pos = {}
for n in T.nodes:
    pos[n] = n

# node_colors = ['RED' if n in path else 'WHITE' for n in T.nodes()]
# edge_colors = [T[u][v][C] for u,v in T.edges()]

plt.figure(figsize=(12, 8))
# nx.draw(T, pos=pos, node_color=node_colors, edge_color=edge_colors, node_size=12)
# plt.savefig('normal_maze.png',facecolor='BLACK')

for u,v in HG.edges:
    HG[u][v][C] = 'WHITE'

for n in HG.nodes:
    if n in pos:
        continue

    hyper_node = n.split('||')[0]
    pos[n] = eval(hyper_node)

src = path[0]
for tgt in path[1:]:
    HG.edges[(src,tgt)][C] = 'RED'
    src = tgt

node_colors = ['RED' if n in path else 'WHITE' for n in HG.nodes()]
edge_colors = [HG[u][v][C] for u,v in HG.edges()]

# nx.draw(HG, pos=pos, node_color=node_colors, edge_color=edge_colors, node_size=12)
# plt.savefig('normal_maze.png',facecolor='BLACK')


print(len(G.nodes), len(G.edges))
print(len(HG.nodes), len(HG.edges))