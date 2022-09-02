import networkx as nx
# import numpy as np
from tqdm import trange
from random import seed, random
import os
import pickle

import util
from Keys import C, W

# SIZES = [10, 25, 50, 75, 100, 125, 150, 175, 200]
MAZES = 10
GRID_SIZE = 250
SIZE = GRID_SIZE**2
START = (0,GRID_SIZE-1)
END = (GRID_SIZE-1,0)

if not os.path.exists('mazes'):
    os.mkdir('mazes')

for SEED in trange(MAZES, leave=False):
    base_path = os.path.join('mazes', f'{SEED}_{GRID_SIZE}')
    if os.path.exists(base_path):
        continue
    else:
        os.mkdir(base_path)

    seed(SEED)
    # np.random.seed(SEED)

    G = nx.grid_graph((GRID_SIZE, GRID_SIZE))
    pos = {}
    for n in G.nodes:
        pos[n] = n

    for u,v in G.edges:
        G.edges[(u,v)][C] = 'BLACK'
        G.edges[(u,v)][W] = random()

    T = nx.minimum_spanning_tree(G) # turn into maze

    HG = T.copy()
    node_lookup = util.build_hyper_graph(HG)

    with open(os.path.join(base_path, 'maze_graph.pkl'), 'wb') as f:
        pickle.dump(G, f)

    with open(os.path.join(base_path, 'maze_hyper_graph.pkl'), 'wb') as f:
        pickle.dump(HG, f)

    with open(os.path.join(base_path, 'node_lookup.pkl'), 'wb') as f:
        pickle.dump(node_lookup, f)




# src = path[0]
# for tgt in path[1:]:
#     T.edges[(src,tgt)][C] = 'RED'
#     src = tgt

# node_colors = ['RED' if n in path else 'BLACK' for n in T.nodes()]
# edge_colors = [T[u][v][C] for u,v in T.edges()]

# nx.draw(T, pos=pos, node_color=node_colors, edge_color=edge_colors, node_size=12)
# nx.draw(T, pos=pos, with_labels=True)
# plt.show()

# for n in HG.nodes:
#     if n in pos:
#         continue

#     hyper_node = n.split('||')[0]
#     pos[n] = eval(hyper_node)

# src = path[0]
# for tgt in path[1:]:
#     HG.edges[(src,tgt)][C] = 'RED'
#     src = tgt

# node_colors = ['RED' if n in path else 'BLACK' for n in HG.nodes()]
# edge_colors = [HG[u][v][C] for u,v in HG.edges()]

# nx.draw(HG, pos=pos, node_color=node_colors, edge_color=edge_colors, node_size=12)

# plt.show()