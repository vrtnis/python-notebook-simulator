# src/graph_builder.py

from graphviz import Digraph

def generate_dependency_graph(graph):
    
    dependency_graph = Digraph('DependencyGraph')
    for parent, children in graph.items():
        dependency_graph.node(parent)
        for child in children:
            dependency_graph.edge(parent, child)
    dependency_graph.render('dependency_graph', format='png', cleanup=True)

def generate_execution_order_graph(execution_order):
    
    execution_graph = Digraph('ExecutionOrder')
    for i in range(len(execution_order) - 1):
        execution_graph.edge(execution_order[i], execution_order[i + 1])
    execution_graph.render('execution_order_graph', format='png', cleanup=True)
