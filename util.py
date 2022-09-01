import networkx as nx

def build_hyper_graph(G: nx.Graph) -> None:
    critical_nodes = [n for n in G.nodes() if G.degree(n) > 2]
    
    for n in critical_nodes:
        next_nodes = list(G.edges(n))
        for _, a_2 in next_nodes:
            if a_2 in critical_nodes:
                continue
            
            G.remove_edge(n, a_2)
            nodes = [str(a_2)]
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
                
                nodes.append(str(a_3))
                G.remove_edge(a_2, a_3)
                G.remove_node(a_2)

                a_1 = a_2
                a_2 = a_3

            hyper_state_name = '||'.join(nodes)
            G.add_edge(n, hyper_state_name)

            if a_1 != None:
                G.add_edge(hyper_state_name, a_3)
