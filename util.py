import networkx as nx

from Keys import W

def build_hyper_graph(G: nx.Graph):
    critical_nodes = [n for n in G.nodes() if G.degree(n) > 2]
    node_lookup = {}

    for n in critical_nodes:
        node_lookup[n] = n
        next_nodes = list(G.edges(n))

        for _, a_2 in next_nodes:
            if a_2 in critical_nodes:
                continue
            
            if not G.has_edge(n, a_2):
                continue

            G.remove_edge(n, a_2)
            weight = 0
            nodes = [a_2]
            a_1 = n
            a_3 = None
            while True:
                if a_2 in critical_nodes:
                    nodes.pop()
                    break   
                
                edges = G.edges(a_2)
                if len(edges) == 0:
                    G.remove_node(a_2)
                    a_1 = None
                    break

                for _, a_3 in G.edges(a_2):
                    if a_1 != a_3:
                        break
                
                weight += G.edges[(a_2, a_3)][W]
                nodes.append(a_3)
                G.remove_edge(a_2, a_3)
                G.remove_node(a_2)

                a_1 = a_2
                a_2 = a_3

            hyper_state_name = '||'.join(str(node_name) for node_name in nodes)
            for node_name in nodes:
                node_lookup[node_name] = hyper_state_name

            critical_nodes.append(hyper_state_name)
            G.add_edge(n, hyper_state_name, weight=weight, color='BLACK')

            if a_1 != None:
                G.add_edge(hyper_state_name, a_3, weight=0, color='BLACK')

    return node_lookup