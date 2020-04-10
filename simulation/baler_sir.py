import numpy as np

class Graph():


    def __init__(self, nodes = None, adj_matrix = None, beta = 0.0001, gamma = 0.75):
        super(Graph, self).__init__()

        self.nodes = nodes
        self.adj_matrix = adj_matrix
        self.time = 0
        self.beta = beta
        self.gamma = gamma
        self.recovered = []

    def recovery_step(self):
        recovered = []
        for i, j in enumerate(self.nodes):

            if j == 1:
                if np.random.binomial(1, self.gamma):
                    recovered.append(i)
                    adjacent_nodes = self.adj_matrix[i]
                    del self.adj_matrix[i]
                    for n in adjacent_nodes:
                        self.adj_matrix[n].remove(i)
                


        for i in recovered:
            self.recovered.append(i)
            np.delete(self.nodes, i)

    def infection_node(self, node = 1):
        if self.nodes[node] == 0:
            neighbor_indices = self.adj_matrix[node]
            neighbor = np.zeros(self.nodes.shape[0])
            neighbor[neighbor_indices] = 1
            score = self.beta * (np.dot(neighbor, self.nodes))
            prob = 1/(1+np.exp(-score))
            self.nodes[node] = np.random.binomial(1, prob)


    def infection_step(self):
        for i, _ in enumerate(self.nodes):
            self.infection_node(i)

    def current_status(self):
        return sum(self.nodes), len(self.recovered)


