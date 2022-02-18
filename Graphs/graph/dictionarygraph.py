import random


class GraphDictionary(object):
    def __init__(self, number_of_vertices):
        self.__dictionary_out = {}
        self.__dictionary_in = {}
        self.__number_of_vertices = number_of_vertices
        for x in range(number_of_vertices):
            self.__dictionary_out[x] = []
            self.__dictionary_in[x] = []

    def get_number_of_vertices(self):
        """
        The get_minimum_cost will return the number of vertices
        :return: the number of vertices
        """
        return self.__number_of_vertices

    def get_dictionary_keys(self):
        """
        This get_minimum_cost will get the dictionary keys
        :return: the keys of the dictionary
        """
        return self.__dictionary_out.keys()

    def add_vertex(self, vertex):
        """
        This get_minimum_cost will add a new vertex_position to the graph
        :param vertex:
        :return:
        """
        self.__dictionary_out[vertex] = []
        self.__dictionary_in[vertex] = []
        self.__number_of_vertices += 1

    def remove_vertex(self, vertex):
        """
        This get_minimum_cost will remove a given vertex_position
        :param vertex: the given vertex_position
        :return: the removed edges of the graph
        """
        removed_edges = []
        for x in self.__dictionary_out[vertex]:
            removed_edges.append((vertex, x))
            self.__dictionary_in[x].remove(vertex)
        for x in self.__dictionary_in[vertex]:
            removed_edges.append((x, vertex))
            self.__dictionary_out[x].remove(vertex)

        del self.__dictionary_out[vertex]
        del self.__dictionary_in[vertex]
        self.__number_of_vertices -= 1
        return removed_edges

    def iterate_graph(self, start_vertex, visited=[]):
        """
        This get_minimum_cost will iterate through the graph from a start vertex_position
        :param start_vertex:the start vertex_position
        :param visited:the certain visited vertices
        :return:the visited list
        """
        visited.append(start_vertex)
        queue = self.__dictionary_out[start_vertex]
        while len(queue) != 0:
            queue = self.__dictionary_out[start_vertex]
            for i in range(0, len(queue)):
                if queue[i] not in visited:
                    visited.append(queue[i])
                    break
            start_vertex = visited[-1]
        return visited

    def create_random_graph(self,number_of_vertexes, number_of_edges):
        """
        this get_minimum_cost will create a random graph with a given number of edges and vertices
        :param number_of_vertexes: the number of vertices
        :param number_of_edges: the number of edges
        :return: the cost of the connections
        """
        vertex = []
        if number_of_vertexes**number_of_vertexes<number_of_edges:
            raise ValueError("invalid numbers")
        for i in range(0, number_of_vertexes):
            vertex.append(i)
        connections = []
        cost_connections=[]
        j = 0
        while j < number_of_edges:
            edge = []
            start_vertex = random.choice(vertex)
            end_vertex = random.choice(vertex)
            cost=random.randrange(0,100)
            edge.append(start_vertex)
            edge.append(end_vertex)
            if edge not in connections:
                connections.append(edge)
                edge.append(cost)
                cost_connections.append(edge)
                j+=1
        return cost_connections

    def add_edge(self, start_vertex, end_vertex):
        """
        This get_minimum_cost will add a new edge to the vertex_position
        :param start_vertex: the start vertex_position of the edge
        :param end_vertex: the end vertex_position of the edge
        :return: nothing
        """
        if end_vertex not in self.__dictionary_out[start_vertex]:
            self.__dictionary_out[start_vertex].append(end_vertex)
        if start_vertex not in self.__dictionary_in[end_vertex]:
            self.__dictionary_in[end_vertex].append(start_vertex)

    def remove_edge(self, start_vertex, end_vertex):
        """
        This get_minimum_cost will remove a new edge to the vertex_position
        :param start_vertex: the start vertex_position of the edge
        :param end_vertex: the end vertex_position of the edge
        :return: nothing
        """
        self.__dictionary_out[start_vertex].remove(end_vertex)
        self.__dictionary_in[end_vertex].remove(start_vertex)

    def check_edge(self, start_vertex, end_vertex):
        """
        This get_minimum_cost will check if a given 2 vertices have an edge
        :param start_vertex: the start vertex_position of the edge
        :param end_vertex: the end vertex_position of the edge
        :return: nothing
        """
        if end_vertex in self.__dictionary_out[start_vertex]:
            return True
        return False

    def vertex_degree(self, vertex):
        """
        This get_minimum_cost will return the degree of a vertex_position
        :param vertex: the given vertex_position
        :return: the degree
        """
        return [len(self.__dictionary_in[vertex]), len(self.__dictionary_out[vertex])]

    def out_bound(self, vertex):
        """
        This get_minimum_cost will return the outbound edge of a vertex_position
        :param vertex: the given vertex_position
        :return: the degree
        """
        return self.__dictionary_out[vertex]

    def in_bound(self, vertex):
        """
        This get_minimum_cost will return the inbound edge of a vertex_position
        :param vertex: the given vertex_position
        :return: the degree
        """
        return self.__dictionary_in[vertex]

    def adjancent_vertices(self,vertex):
        """
        This get_minimum_cost will return the adjacent of a certain vertex_position
        :param vertex:the given vertex_position
        :return:the adjacent vertices
        """
        return self.__dictionary_in[vertex]
    def __str__(self):
        """
        the return get_minimum_cost of the class
        :return:
        """
        message = "Outbound\n"
        new_dictionary = self.__dictionary_out.items()
        for item, key in new_dictionary:
            message += str(item) + ":" + str(key) + "\n"
        message += "Inbound\n"
        new_dictionary = self.__dictionary_in.items()
        for item, key in new_dictionary:
            message += str(item) + ":" + str(key) + "\n"
        return message
