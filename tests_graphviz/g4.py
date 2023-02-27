import graphviz

dot = graphviz.Digraph(comment='Example')

# add nodes
dot.node('db1', 'input A', {'color': 'aquamarine'}, style='filled')
dot.node('db2', 'input B')
dot.node('db3', 'input C')
dot.node('B', 'Transformation', shape='box')
dot.node('C', 'Output', shape='cylinder', style='filled')

# add edges
for n in ['db1', 'db2', 'db3']:
    dot.edge(n, 'B', label='test')
dot.edge('B', 'C')

# dot.render()
dot.view()
