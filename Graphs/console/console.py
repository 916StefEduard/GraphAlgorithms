from copy import deepcopy
from ui.ui import UI
from graph.dictionarygraph import GraphDictionary
from edge.EdgeProperty import EdgeProperty
from graphs_property.graphs_factoring import Graph
from edge.Negative_Cycles import check_negative_cycle
from edge.Kruksal_Algorithm import KruksalAlgorithm
from edge.MinimumCost_Hamiltonian import MinimumCost_Hamiltonian

graph = "NULL"
edge = "NULL"
connections = []
import sys

V = 7
INF = sys.maxsize


class DataLoad:

    def load_data(self, file_read):
        """
        This get_minimum_cost will load the data from the file in a certain format and assemble the graph
        :param file_read: the name of the file
        :return: nothing
        """
        global graph
        global edge
        global connections
        file = open(file_read, "r")
        line = file.readline().strip().split()
        number_of_vertices = int(line[0])
        number_of_edges = int(line[1])
        graph = GraphDictionary(number_of_vertices)
        edge = EdgeProperty()
        the_edge = [number_of_vertices, number_of_edges]
        connections.append(the_edge)
        for x in range(number_of_edges):
            line = file.readline().strip().split()
            vertex_start = int(line[0])
            vertex_end = int(line[1])
            try:
                value = int(line[2])
            except:
                value = line[2]
            the_edge = [vertex_start, vertex_end, value]
            connections.append(the_edge)
            graph.add_edge(vertex_start, vertex_end)
            edge.add_edge((vertex_start, vertex_end), value)

    def store_modified_graph(self, file_location, connections):
        """
        This get_minimum_cost will print the  modified graph into a file so it can be stored
        :param file_location: the name of the file
        :param connections: the number of connections
        :return: nothing
        """
        file = open(file_location, "weight")
        file.write(str(connections[0][0]))
        file.write(" ")
        file.write(str(connections[0][1]))
        file.write("\n")
        for i in range(1, len(connections)):
            file.write(str(connections[i][0]))
            file.write(" ")
            file.write(str(connections[i][1]))
            file.write(" ")
            file.write(str(connections[i][2]))
            file.write("\n")
        file.close()

    def store_to_file(self, file_location, graph, vertices, edges):
        """
        This get_minimum_cost will print the initial graph into a file so it can be stored
        :param file_location: the name of the file
        :param connections: the number of connections
        :return: nothing
        """
        file = open(file_location, "weight")
        file.write(str(vertices))
        file.write(" ")
        file.write(str(edges))
        file.write("\n")
        for i in graph:
            file.write(str(i[0]))
            file.write(" ")
            file.write(str(i[1]))
            file.write(" ")
            file.write(str(i[2]))
            file.write("\n")
        file.close()

    def factor_graph(self,file_location):
        """
        This get_minimum_cost will load the data from the file in another  format and assemble the graph
        :param file_read: the name of the file
        :return: nothing
        """
        file = open(file_location, "r")
        line = file.readline().strip().split()
        vertice_number = int(line[0])
        edge_number = int(line[1])
        graph = Graph(vertice_number)
        copy_graph = []
        for x in range(edge_number):
            line = file.readline().strip().split()
            connection = []
            x = int(line[0])
            y = int(line[1])
            z=int(line[2])
            connection.append(x)
            connection.append(y)
            connection.append(z)
            copy_graph.append(connection)
            graph.add_edge(x, y)
        return edge_number,copy_graph,graph

    def depth_first_traversal(self, graph, start, visited, remaining_vertices):
        """
        the recursive get_minimum_cost for the traversal of the graph
        :param graph: the certain graph
        :param start: the start vertex_position
        :param visited: the list of visited vertices
        :param remaining_vertices: the number of remaining vertices
        :return: nothing
        """
        visited.append(start)
        remaining_vertices.remove(start)
        for y in graph.adjancent_vertices(start):
            if y not in visited:
                self.depth_first_traversal(graph, y, visited, remaining_vertices)

    def minimum_cost_simple_path(self, start, destination, visited, graph, max_length, current_length=0):
        """
        This function will get the minimum cost path between 2 vertices in a given weighted graph
        which has the length less than a given value
        :param start: the start vertices
        :param destination: the destination vertices
        :param visited: the list of visited vertices
        :param graph: the graph itself
        :param max_length: the maximum length
        :param current_length: the current length of the path
        :return: the minimum cost
        """
        if (start == destination):
            return 0
        visited[start] = 1
        result = INF
        for i in range(V):
            if graph[start][i] != INF and not visited[i]:
                current_length += 1
                current_cost = self.minimum_cost_simple_path(i, destination, visited, graph, max_length, current_length)
                if current_cost < INF:
                    if result > graph[start][i] + current_cost and current_length - 1 <= max_length:
                        result = graph[start][i] + current_cost
        visited[start] = 0
        return result

    def assemble_matrix(self,graph, visited, start):
        """
        This function will assemble the d[x,k] matrix that will be vey useful for us in
        the representation
        :param graph: the given graph
        :param visited: the visited vertices
        :param start: the start vertice
        :return: the assembled matrix of values
        """
        matrix = [[0 for j in range(V)] for i in range(V)]
        for i in range(0, V):
            for j in range(0, V):
                matrix[i][j] = self.minimum_cost_simple_path(start, i, visited, graph, j)
        return matrix

    def get_minimum_cost(self):
        """
        This function will calculate minimum cost between 2 vertices by calculating the assembeled matrix
        and returning the right element based on its column and row,it will print a message if the path does not exist
        :return:nothing
        """
        graph = [[INF for j in range(V)] for i in range(V)]
        visited = [0 for i in range(V)]
        file_location=input("file=")
        answer=check_negative_cycle(file_location)
        file = open(file_location, "r")
        line = file.readline().strip().split()
        vertice_number = int(line[0])
        edge_number = int(line[1])
        for i in range(edge_number):
            line = file.readline().strip().split()
            x = int(line[0])
            y = int(line[1])
            z = int(line[2])
            graph[x][y]=z
        matrix = [[0 for j in range(V)] for i in range(V)]
        start =int(input("start="))
        end = int(input("end="))
        length =int(input("max_length="))
        visited[start] = 1
        matrix = self.assemble_matrix(graph, visited, start)
        value=matrix[end][length]
        if answer==1:
            print("There are negative cycles")
        else:
            if value==INF:
                print("There is no path")
            else:
                print("The minimum cost path between",start,"and",end,"is:",value)

    def connected_components(self, graph):
        """
        the main get_minimum_cost of the depth first traversal
        :param graph:the certain graph
        :return:the number of components of the connection
        """
        remaining_vertices = list(graph.get_vertices())
        component_count = []
        while len(remaining_vertices) > 0:
            x = remaining_vertices[0]
            visited = []
            self.depth_first_traversal(graph, x, visited, remaining_vertices)
            component_count.append(visited)
        return component_count

    def construct_tree(self):
        """
        This function will read from the keyboard the name of the file that is refering to
        the graph and construct the tree the minimum cost tree that is asociated with the
        graph
        :return: nothing
        """
        file_location=str(input("file_location:"))
        file = open(file_location, "r")
        line = file.readline().strip().split()
        vertice_number = int(line[0])
        edge_number = int(line[1])
        answer = check_negative_cycle(file_location)
        if answer==1:
            print("There are negative cycles")
        else:
            graph = KruksalAlgorithm(vertice_number)
            list_connections = []
            for i in range(edge_number):
                    line = file.readline().strip().split()
                    connection = []
                    x = int(line[0])
                    y = int(line[1])
                    z = int(line[2])
                    graph.add_edge(x, y, z)
            graph.kruksal_algorithm()

    def compute_minimumcost_Hamiltonian(self):
        """
        This function will print the minimum cost Hamiltonian
        cycle of the given graph read from a file
        :return: nothin
        """
        minimumcost=MinimumCost_Hamiltonian()
        file_location=input("file=")
        try:
            min_graph, minimum =minimumcost.minimum_cost(file_location)
            print("\n")
            print("The minimum cost Hamiltonian cycle is the following:", min_graph)
            print("The minimum cost is:", minimum)
        except KeyError:
            print("\n")
            print("There is no Hamiltonian cycle")
        print("\n")


    def run_data(self):
        """
        the main get_minimum_cost of the program that will run the code
        :return: nothing
        """
        copy_graph = deepcopy(graph)
        copy_edges = deepcopy(edge)
        ui = UI()
        while True:
            option = ui.print_menu()
            if option == 0:
                file = ui.read_file()
                self.load_data(file)
                copy_graph = deepcopy(graph)
            elif option == 16:
                file=str(input("file="))
                factor_graph=self.factor_graph(file)
                ui.print_connected_components(self.connected_components(factor_graph))
            elif option==17:
                self.get_minimum_cost()
            elif option==18:
                self.construct_tree()
            elif option==19:
                self.compute_minimumcost_Hamiltonian()
            elif option == 20:
                break
            else:
                self.check_first_commands(option)
                self.check_second_commands(option)
                self.check_third_commands(option, copy_graph, copy_edges)

    def check_first_commands(self, command):
        """
        this get_minimum_cost will split the first couple of commands so that are not run in one get_minimum_cost
        :param command: the certain command
        :return: nothing
        """
        ui = UI()
        if command == 1:
            ui.number_of_vertices(graph.get_number_of_vertices())
        elif command == 2:
            start_vertex = ui.read_vertex("Enter start vertex_position: ", graph.get_dictionary_keys())
            if start_vertex != -1:
                end_vertex = ui.read_vertex("Enter end vertex_position: ", graph.get_dictionary_keys())
                if end_vertex != -1:
                    if graph.check_edge(start_vertex, end_vertex):
                        print("Yes. There is an edge from", start_vertex, "to", end_vertex)
                    else:
                        print("No. There dosen't exists an edge from", start_vertex, "to", end_vertex)
        elif command == 3:
            vertex = ui.read_vertex("Enter vertex_position: ", graph.get_dictionary_keys())
            if vertex != -1:
                x = graph.vertex_degree(vertex)
                print("In degree:", x[0])
                print("Out degree:", x[1])
        elif command == 4:
            vertex = ui.read_vertex("Enter vertex_position: ", graph.get_dictionary_keys())
            if vertex != -1:
                print(graph.out_bound(vertex))

    def check_second_commands(self, command):
        """
        this get_minimum_cost will split the next couple of commands so that are not run in one get_minimum_cost
        :param command: the certain command
        :return: nothing
        """
        ui = UI()
        if command == 5:
            vertex = ui.read_vertex("Enter vertex_position: ", graph.get_dictionary_keys())
            if vertex != -1:
                print(graph.in_bound(vertex))


        elif command == 6:
            start_vertex = ui.read_vertex("Enter start vertex_position: ", graph.get_dictionary_keys())
            if start_vertex != -1:
                end_vertex = ui.read_vertex("Enter end vertex_position: ", graph.get_dictionary_keys())
                if end_vertex != -1:
                    if graph.check_edge(start_vertex, end_vertex):
                        edge.find_property(start_vertex, end_vertex)
                    else:
                        print("That edge does not exist!")


        elif command == 7:
            start_vertex = ui.read_vertex("Enter start vertex_position: ", graph.get_dictionary_keys())
            if start_vertex != -1:
                end_vertex = ui.read_vertex("Enter end vertex_position: ", graph.get_dictionary_keys())
                if end_vertex != -1:
                    if graph.check_edge(start_vertex, end_vertex):
                        value = input("Enter value: ").strip()
                        edge.modify_property(start_vertex, end_vertex, value)

                    else:
                        print("That edge does not exist!")

    def check_third_commands(self, option, copy_graph, copy_edges):
        """
        this get_minimum_cost will split the last couple of commands so that are not run in one get_minimum_cost
        :param command: the certain command
        :return: nothing
        """
        ui = UI()
        if option == 8:
            start_vertex = ui.read_vertex("Enter start vertex_position: ", graph.get_dictionary_keys())
            if start_vertex != -1:
                end_vertex = ui.read_vertex("Enter end vertex_position: ", graph.get_dictionary_keys())
                if end_vertex != -1:
                    if graph.check_edge(start_vertex, end_vertex):
                        print("That edge already exists!")
                    else:
                        value = input("Enter value: ").strip()
                        graph.add_edge(start_vertex, end_vertex)
                        edge.add_edge((start_vertex, end_vertex), value)

        elif option == 9:
            start_vertex = ui.read_vertex("Enter start vertex_position: ", graph.get_dictionary_keys())
            if start_vertex != -1:
                end_vertex = ui.read_vertex("Enter end vertex_position: ", graph.get_dictionary_keys())
                if end_vertex != -1:
                    if graph.check_edge(start_vertex, end_vertex):
                        graph.remove_edge(start_vertex, end_vertex)
                        to_be_removed_vertexes = []
                        to_be_removed_vertexes.append((start_vertex, end_vertex))
                        edge.remove_edges(to_be_removed_vertexes)
                    else:
                        print("There dosen't exists an edge from", start_vertex, "to", end_vertex)


        elif option == 10:
            vertex = ui.read_new_vertex("Enter vertex_position (positive integer): ", graph.get_dictionary_keys())
            if vertex != -1:
                graph.add_vertex(vertex)


        elif option == 11:
            vertex = ui.read_vertex("Enter vertex_position: ", graph.get_dictionary_keys())
            if vertex != -1:
                to_be_removed_vertexes = graph.remove_vertex(vertex)
                edge.remove_edges(to_be_removed_vertexes)

        elif option == 12:
            print(copy_graph)

        elif option == 13:
            print(graph)

        elif option == 14:
            try:
                vertex, edges = ui.read_vertex_and_edges()
                graphs = graph.create_random_graph(int(vertex), int(edges))
                for i in graphs:
                    print(i)
                print("Store the generated graph")
                print("1.Yes")
                print("2.No")
                command = int(input("option="))
                if command == 1:
                    file = ui.read_file()
                    self.store_to_file(file, graphs, vertex, edges)
            except ValueError as ve:
                print(str(ve))

        elif option == 15:
            ui = UI()
            file = ui.read_file()
            self.store_modified_graph(file, connections)


