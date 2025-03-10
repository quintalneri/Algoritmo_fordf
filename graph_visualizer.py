import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(edges, flow, source, sink):

    G = nx.DiGraph()
    edge_labels = {}


    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
        flujo = flow[u][v] if v in flow[u] else 0
        residuo = capacity - flujo
        edge_labels[(u, v)] = f"{flujo}/{capacity} ({residuo})"


    path_edges = [(u, v) for u, v in G.edges if flow[u][v] > 0]


    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))


    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
            node_size=2000, font_size=10, width=2)


    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)


    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3)

    plt.title("Grafo con flujo y capacidad")
    plt.show()
