from graphviz import Digraph
from IPython.display import Image

nodes = Digraph()
nodes.node('A', style = 'filled', fillcolor = 'lightyellow', color = 'blue', shape = 'rectange')
nodes.node('B', style = 'filled', fillcolor = 'lightblue', color = 'red', shape = 'circle')
nodes.node('C', style = 'filled', fillcolor = 'lightgreen', color = 'darkgreen', shape = 'circle')
nodes.node('D')
nodes.node('E')
nodes.edge('A','B', label = '10')
nodes.edge('A','C', label = '4')
nodes.edge('B','C', label = '7')
nodes.edge('B','D', label = '1')
nodes.edge('C','D', label = '8')
nodes.edge('D','E', label = '6')


nodes.render('graph', format = 'png' )
display(Image('graph.png'))