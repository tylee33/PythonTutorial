import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_edge('a','b',weight=0.6)
G.add_edge('a','c',weight=0.2)
G.add_edge('c','d',weight=0.1)
G.add_edge('c','e',weight=0.5)
G.add_edge('c','f',weight=0.4)
G.add_edge('a','d',weight=1.3)

elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']>0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']<=0.5 and d['weight']>0.3]
eminor=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']<=0.3]

pos=nx.shell_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=700,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=elarge,width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,width=6,alpha=0.5,edge_color='b',style='dashed')
nx.draw_networkx_edges(G,pos,edgelist=eminor,width=1,edge_color='b',style='dotted')

eLa={}
for i in G.edges_iter():
    eLa[i]=str(i)

nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=eLa,font_size=10)
plt.axis('off')
plt.show()
