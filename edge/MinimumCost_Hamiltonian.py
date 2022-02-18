import sys
INF = sys.maxsize

class MinimumCost_Hamiltonian():

    def Compute_all_Hamiltonian(self, graph, visited=[]):
        """
        This function will compute the hamiltonian cycles of the given graph
        :param graph: the certain graph
        :param visited: the visited vertices of the graph
        :return: nothing
        """
        if not visited:
            for n in graph:
                for i in self.Compute_all_Hamiltonian(graph, [n]):
                    yield i
        else:
            destination = set(graph[visited[-1]]) - set(visited)
            if not destination and len(visited) == len(graph):
                yield visited
            for n in destination:
                for i in self.Compute_all_Hamiltonian(graph, visited + [n]):
                    yield i


    def load_data_from_file(self,file):
        """
        This function will load the data from a file and store it into a graph dictionary
        and into a list named connections;
        :file: the given file of from where we read the output
        :return: the dictionary and the list
        """
        file = open(file)
        vertex_number = 0
        connections = []
        for i in file:
            tokens = i.split(" ")
            vertex_number = tokens[0]
            break
        for i in file:
            tokens = i.split(" ")
            vertex = tokens[0]
            edges = tokens[1]
            cost_vertexes = [vertex, edges]
            if len(tokens) >= 2:
                cost = tokens[2].split("\n")
                cost_vertexes.append(cost[0])
            connections.append(cost_vertexes)
        graph = {}
        for i in range(0, len(connections)):
            graph[connections[i][0]] = 0
        for i in range(0, len(connections)):
            if graph[connections[i][0]] == 0:
                graph[connections[i][0]] = connections[i][1]
            else:
                string = ''
                string += graph[connections[i][0]]
                string += connections[i][1]
                graph[connections[i][0]] = string
        return vertex_number, graph, connections

    def set_matrix(self,file):
        """
        This function will take the list of vertices from the previous function
        and compute a matrix where the values are 0 if the edge does not exist
        and the cost if the edge exists
        :file: the given file of from where we read the output
        :return: the certain matrix
        """
        vertex, graph, connections = self.load_data_from_file(file)
        matrix = [[0 for i in range(int(vertex) + 1)] for j in range(int(vertex) + 1)]
        for i in range(0, len(connections)):
            line = int(connections[i][0])
            row = int(connections[i][1])
            cost = int(connections[i][2])
            matrix[line][row] = cost
        return matrix

    def minimum_cost(self,file):
        """
        This function will compute the minimum cost of all of the
        hamiltonian cycles in the graph and return the cycles,as well
        as the minimum cost
        :file: the given file of from where we read the output
        :return: the minimum cost and the cycle of the cost
        """
        vertex, graph, connections = self.load_data_from_file(file)
        graph = self.Compute_all_Hamiltonian(graph)
        matrix = self.set_matrix(file)
        minimum = 9999999
        total_cost = 0
        min_graph = []
        for i in graph:
            total_cost = 0
            for j in range(0, len(i) - 1):
                cost = matrix[int(i[j])][int(i[j + 1])]
                total_cost += cost
            if total_cost < minimum:
                minimum = total_cost
                min_graph = i
        set_graph = []
        for i in min_graph:
            set_graph.append(int(i))
        return set_graph, minimum
