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
# nx.draw(G, node_color=colors)
# plt.show()

print(G)
util.build_hyper_graph(G)
print(G)