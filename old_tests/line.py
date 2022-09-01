import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from random import seed

import util


G = nx.Graph()
G.add_edge(0,1, weight=1, color='BLACK')
G.add_edge(1,2, weight=1, color='BLACK')
G.add_edge(2,3, weight=1, color='BLACK')
G.add_edge(3,4, weight=1, color='BLACK')
G.add_edge(4,5, weight=1, color='BLACK')
G.add_edge(5,6, weight=1, color='BLACK')

G.add_edge( 1, 10, weight=1, color='BLACK')
G.add_edge(10, 11, weight=1, color='BLACK')
G.add_edge(11, 12, weight=1, color='BLACK')

G.add_edge( 2, 20, weight=1, color='BLACK')

# path = nx.astar_path(G, 0, 2, weight='weight')
# print(path)

HG = G.copy()
util.build_hyper_graph(HG)

print(HG.nodes())
print(HG.edges())
# nx.draw(HG)
# plt.show()