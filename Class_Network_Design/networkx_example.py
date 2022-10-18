import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1, 3)
G.add_edge(4, 2)
G.add_edge(3, 2)
G.add_edge(1, 5)
G.add_edge(4, 3)
G.add_edge(2, 1)

nx.draw_networkx(G)
plt.figure()
plt.draw_all()
