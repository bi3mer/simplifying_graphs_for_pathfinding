import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from random import seed

import util

SEED = 2
seed(SEED)
np.random.seed(SEED)

G: nx.Graph = nx.circulant_graph(10, [1])
G.add_edge(0, 5)
G.add_edge(0, 11)
G.add_edge(11,12)
G.add_edge(12,13)
G.add_edge(13,14)

HG = G.copy()
util.build_hyper_graph(HG)

print(f'{len(G.nodes)} vs {len(HG.nodes)}')
print(f'{len(G.edges)} vs {len(HG.edges)}')

nx.draw(HG)
plt.show()