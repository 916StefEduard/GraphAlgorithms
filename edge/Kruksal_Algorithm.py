from collections import defaultdict


class KruksalAlgorithm:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, start, end, weight):
        """
        This function will add an edge to the existing graph
        :param start: the start vertex
        :param end: the end vertex
        :param weight:the weight of the graph
        :return:nothing
        """
        self.graph.append([start, end, weight])

    def find(self, parent, i):
        """
        This function will find with recursion a vertex in an existing graph
        :param parent: the parent vertex
        :param i: the end point
        :return: the function recursed
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        This function will make a union of points in a graph
        by their rank
        :param parent: the parent vertex
        :param rank: the rank of the vertex
        :param x: start vertex
        :param y: end vertex
        :return: nothing
        """
        start_root = self.find(parent, x)
        end_root = self.find(parent, y)
        if rank[start_root] < rank[end_root]:
            parent[start_root] = end_root
        elif rank[start_root] > rank[end_root]:
            parent[end_root] = start_root
        else:
            parent[end_root] = start_root
            rank[start_root] += 1

    def kruksal_algorithm(self):
        """
        This function is the Kruksal algorithm itself, which calculates
        the minimum cost tree that will be obtained from a given graph.
        :return: nothing
        """
        result = []
        i = 0
        edge = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while edge < self.vertices - 1:
            start, end, weight = self.graph[i]
            i = i + 1
            x = self.find(parent, start)
            y = self.find(parent, end)
            if x != y:
                edge = edge + 1
                result.append([start, end, weight])
                self.union(parent, rank, x, y)
        minimum_cost = 0
        print("\n")
        print("Edges in the constructed Tree:")
        print("\n")
        for start, end, weight in result:
            minimum_cost += weight
            print("  start:%d | end:%d | cost:%d" % (start, end, weight))
        print("\n")
        print("Minimum Cost of the Tree:", minimum_cost)

