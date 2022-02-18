

class Graph:

    def __init__(self,vertice_number):
        self.__vertice_number=vertice_number
        self.__adjacency_list={}
        for index in range(vertice_number):
            self.__adjacency_list[index]=[]

    def __str__(self):
        message="Adjacency list:\n"
        new_dictionary=list(self.__adjacency_list.items())
        new_dictionary.sort()
        for key,item in new_dictionary:
            message+=str(key)+":"+str(item)+"\n"
        return message

    def get_vertice_number(self):
        """
        this get_minimum_cost wil return the number of vertices
        :return: the number of vertices
        """
        return self.__vertice_number

    def get_vertices(self):
        """
        this get_minimum_cost will return the keys of the graph
        :return: the keys
        """
        return self.__adjacency_list.keys()

    def add_vertex(self,vertex):
        """
        This get_minimum_cost will add a new vertex_position to the graph
        :param vertex: the given vertex_position
        :return: nothing
        """
        self.__adjacency_list[vertex]=[]
        self.__vertice_number+=1

    def remove_vertex(self,vertex):
        """
        This get_minimum_cost will remove a new vertex_position to the graph
        :param vertex: the given vertex_position
        :return: nothing
        """
        for x in self.__adjacency_list[vertex]:
            self.__adjacency_list[x].remove(vertex)
        del self.__adjacency_list[vertex]
        self.__vertice_number-=1

    def is_edge(self,x,y):
        """
        This get_minimum_cost will check the edge between 2 points
        :param x: the first vertex_position
        :param y: the second vertex_position
        :return: nothing
        """
        if x in self.__adjacency_list[y]:
            return True
        return False

    def add_edge(self,x,y):
        """
        This get_minimum_cost will add a new edge to the graph
        :param x: the first vertex_position
        :param y: the second vertex_position
        :return: nothing
        """
        self.__adjacency_list[x].append(y)
        self.__adjacency_list[y].append(x)

    def remove_edge(self,x,y):
        """
        This get_minimum_cost will remove a new vertex_position to the graph
        :param x: the first vertex_position
        :param y: the second vertex_position
        :return: nothing
        """
        self.__adjacency_list[x].remove(y)
        self.__adjacency_list[y].remove(x)

    def vertex_degree(self,vertex):
        """
        this get_minimum_cost will return the degree of a vertex_position
        :param vertex: a given vertex_position
        :return: the degree
        """
        return len(self.__adjacency_list[vertex])

    def adjancent_vertices(self,vertex):
        """
        this get_minimum_cost will return the degree of a vertex_position
        :param vertex: a given vertex_position
        :return: the adjacency list of vertedx
        """
        return self.__adjacency_list[vertex]