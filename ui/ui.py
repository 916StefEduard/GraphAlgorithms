
class UI(object):

    def read_new_vertex(self, message, keys):
        """
        ui get_minimum_cost for reading a new vertex_position
        :param message: the message
        :param keys: the key of the vertex_position
        :return: the message
        """
        x = input(message).strip()
        while x in str(keys) and x != "c":
            print("That was not a positive integer or vertex_position already exists!")
            print('Enter "c" to cancel operation.')
            x = input(message).strip()
        if x == "c":
            return -1
        return int(x)

    def read_vertex(self, message, keys):
        """
        ui get_minimum_cost for reading a new vertex_position
        :param message: the message
        :param keys: the key of the vertex_position
        :return: the message
        """
        x = input(message).strip()
        while x not in str(keys) and x != "c":
            print("That vertex_position does not exist!")
            print('Enter "c" to cancel operation.')
            x = input(message).strip()
        if x == "c":
            return -1
        return int(x)

    def read_file(self):
        """
        this get_minimum_cost will read the name of a file
        :return: the file name
        """
        file = input("text file:")
        return file

    def read_vertex_and_edges(self):
        """
        this get_minimum_cost will read a new vertex_position and number of edges
        :return: the vertex_position and edges
        """
        vertex = input("Number of vertices=")
        edges = input("Number of edges=")
        return vertex, edges

    def number_of_vertices(self, number_of_vertices):
        """
        this get_minimum_cost will read a number of vertices
        :param number_of_vertices: the certain number of vertices
        :return: nothing
        """
        print("Number of vertices:", number_of_vertices)

    def print_connected_components(self, connected_components):
        """
        the ui get_minimum_cost for printing connected graph
        :param connected_components: the connected components
        :return: nothing
        """
        counter = 1
        for x in connected_components:
            print("Connected component number", counter)
            print(x)
            counter += 1

    def print_menu(self):
        """
        this get_minimum_cost will print the menu of the application
        :return:
        """
        print("\n")
        print("0.read the graph from the file")
        print("1.get the number of vertices.")
        print("2.check if there is an edge between two vertices.")
        print("3.show the in and out degree of a vertex_position.")
        print("4.out_bound edges of a specified vertex_position.")
        print("5.in_bound edges of a specified vertex_position.")
        print("6.retrieve the value attached to an edge.")
        print("7.modify the value attached to an edge.")
        print("8.add a new edge.")
        print("9.remove a edge.")
        print("10.add a new vertex_position.")
        print("11.remove a vertex_position.")
        print("12.show the initial graph.")
        print("13.show graph.")
        print("14.create random graph")
        print("15.write a graph to a file")
        print("16.connected components of depth first traversal")
        print("17.minimum cost walk using a matrix")
        print("18.constructs a minumal spanning tree using the Kruskal's algorithm")
        print("19.compute the minimum cost Hamiltonian graph")
        print("20.exit")
        option = input("Enter option: ")
        return int(option)
