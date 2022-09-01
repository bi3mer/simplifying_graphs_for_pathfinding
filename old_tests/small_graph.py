import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from random import seed

import util

SEED = 2
seed(SEED)
np.random.seed(SEED)

G = nx.watts_strogatz_graph(25, 3, 0.8)
path = nx.astar_path(G, 22, 8)
colors = ['GREEN' if n in path else 'BLACK' for n in G.nodes()]

HG = G.copy()
util.build_hyper_graph(HG)

print(f'{len(G.nodes)} vs {len(HG.nodes)}')
print(f'{len(G.edges)} vs {len(HG.edges)}')
