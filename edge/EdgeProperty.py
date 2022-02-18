

class EdgeProperty(object):
    def __init__(self):
        self.__dictionary = {}

    def add_edge(self, key, value):
        """
        this get_minimum_cost will add a new edge to the graph
        :param key:the key of the edge
        :param value:the value of the edge
        :return:nothing
        """

        try:
            value = int(value)
        except:
            pass
        self.__dictionary[key] = value

    def remove_edges(self, removed_edges):
        """
        this get_minimum_cost will remove a new edge to the graph
        :param key:the key of the edge
        :param value:the value of the edge
        :return:nothing
        """
        for x in removed_edges:
            del self.__dictionary[x]

    def find_property(self, start_vertex, end_vertex):
        """
        This get_minimum_cost will find the cost of 2 vertices
        :param start_vertex: first vertex_position
        :param end_vertex: second vertex_position
        :return: nothing
        """
        key = (start_vertex, end_vertex)
        print("The value of the edge from", start_vertex, "to", end_vertex, "is:", self.__dictionary[key])

    def modify_property(self, start_vertex, end_vertex, value):
        """
        this get_minimum_cost will modify the property of 2 given vertices
        :param start_vertex: the first vertex_position
        :param end_vertex: the second vertex_position
        :param value: the value between the two
        :return: nothing
        """
        key = (start_vertex, end_vertex) 
        try:
            value = int(value)
        except:
            value = value
        self.__dictionary[key] = value
        
    def __str__(self): 
        message = "" 
        new_dictionary = self.__dictionary.items()
        for item, key in new_dictionary: 
            message += str(item) + ":" + str(key) + "\n"
        return message

