import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from random import seed

import util


G = nx.Graph()
G.add_edge(0,2, weight=0.5)
G.add_edge(0,1, weight=0.1)
G.add_edge(0,2, weight=0.1)

path = nx.astar_path(G, 0, 2, weight='weight')
print(path)