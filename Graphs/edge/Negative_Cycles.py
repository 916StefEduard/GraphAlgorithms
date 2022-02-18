class Edge:

    def __init__(self):
        self.start = 0
        self.end = 0
        self.weight = 0


class Graph:

    def __init__(self):
        self.vertice_postion = 0
        self.edge_position = 0
        self.edge = None


def createGraph(vertice_number, edge_number):
    """
    This function will create a graph based on the number of
    vertices and edges of the certain graph
    :param vertice_number: the given number of vertices
    :param edge_number: the given number of edges
    :return: will return the graph
    """
    graph = Graph()
    graph.vertice_postion = vertice_number
    graph.edge_position = edge_number
    graph.edge = [Edge() for i in range(graph.edge_position)]
    return graph


def Bellman_Ford(graph, start):
    """
    This function will check if the given grapg contains negative cost cycles
    or not
    :param graph: the given graph of elements
    :param start: the start vertex of the graph
    :return: False or true depending on the result
    """
    vertice_number = graph.vertice_postion
    edge_number = graph.edge_position
    distance = [1000000 for i in range(vertice_number)]
    distance[start] = 0

    for i in range(1, vertice_number):
        for j in range(edge_number):

            u = graph.edge[j].start
            v = graph.edge[j].end
            weight = graph.edge[j].weight
            if distance[u] != 1000000 and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    for i in range(edge_number):

        u = graph.edge[i].start
        v = graph.edge[i].end
        weight = graph.edge[i].weight
        if distance[u] != 1000000 and distance[u] + weight < distance[v]:
            return True

    return False


def check_negative_cycle(file_location):
    """
    This function will load the data from the file into a graph
    and then check if the graph has negative cost cycles
    :param file_location: the name of the file
    :return: 1 or 0 depending on the result
    """
    file = open(file_location, "r")
    line = file.readline().strip().split()
    vertice_number = int(line[0])
    edge_number = int(line[1])
    graph = createGraph(vertice_number, edge_number)
    list_connections = []
    for i in range(edge_number):
        line = file.readline().strip().split()
        connection = []
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])
        connection.append(x)
        connection.append(y)
        connection.append(z)
        list_connections.append(connection)
    for i in range(edge_number):
        graph.edge[i].start = list_connections[i][0]
        graph.edge[i].end = list_connections[i][1]
        graph.edge[i].weight = list_connections[i][2]

    if Bellman_Ford(graph, 0):
        return 1
    else:
        return 0
