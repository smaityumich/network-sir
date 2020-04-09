import numpy as np

class Graph():


    def __init__(self, nodes = None, adj_matrix = None, beta = 0.01, gamma = 0.02):
        super(Graph, self).__init__()

        self.nodes = nodes
        self.adj_matrix == adj_matrix
        self.time = 0
        self.beta = beta
        self.gamma = gamma

    def node_propagation(self, node = 1):
        
