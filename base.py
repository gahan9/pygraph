"""
reference: https://www.python.org/doc/essays/graphs/
BASIC structure of graph:
    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
"""
from pprint import pprint


class Graph(object):
    def __init__(self, *args, **kwargs):
        # This(self.default_graph) is a dictionary whose keys are the nodes of the graph.
        # For each key, the corresponding value is a list containing the nodes
        # that are connected by a direct arc from this node
        self.default_graph = {'A': ['B', 'C'],
                              'B': ['C', 'D'],
                              'C': ['D'],
                              'D': ['C'],
                              'E': ['F'],
                              'F': ['C']}

    def find_path(self, graph, start, end, path=[]):
        """
        simple function to determine a path between two nodes
        algorithm paradigm: backtracking
        :param graph: graph
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
                    This argument is used to avoid cycles
        :return:a list of nodes (including the start and end nodes) comprising the path.
                When no path can be found, it returns None
        """
        path = path + [start]  # creates a new list.
        # If we had written "path.append(start)" instead,
        # we would have modified the variable 'path' in the caller
        if start == end:
            return path  # start and end node are same
        if start not in graph:
            return None  # graph does not contain given start node
        for node in graph[start]:  # explore nodes in corresponding start node
            if node not in path:  # If current node is unexplored then proceed ahead
                new_path = self.find_path(graph, node, end,
                                          path)  # find path from current node(as start node) to end node
                if new_path:
                    return new_path  # if new_path found between nodes then return the new_path
        return None  # no path can be found, returns None

    def find_all_paths(self, graph, start, end, path=[]):
        """
        find all paths from one node to other in given graph
        :param graph: graph structure
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
        :return: all explored paths
        """
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []  # maintain a list to store all explored path
        for node in graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)  # add new path to list instead of returning it.
        return paths

    def find_shortest_path(self, graph, start, end, path=[]):
        """
        find shortest path from one node to other in given graph
        :param graph: graph structure
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
        :return: shortest path between two nodes
        """

        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None  # maintain a variable to check with every new explored path, replace existing with shortest one
        for node in graph[start]:
            if node not in path:
                new_path = self.find_shortest_path(graph, node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest


if __name__ == "__main__":
    graph_obj = Graph()  # Graph object
    # construct a basic graph
    my_graph = {'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': ['C'],
                'E': ['F'],
                'F': ['C']}
    print("Input graph-")
    pprint(my_graph)  # print input graph
    # find path
    print("Get path from start to end nodes: {}".format(graph_obj.find_path(my_graph, 'A', 'D')))
    # find all path
    print("All paths from start to end node: {}".format(graph_obj.find_all_paths(my_graph, 'A', 'D')))
    # find shortest path
    print("Get Shortest paths from start to end node: {}".format(graph_obj.find_shortest_path(my_graph, 'A', 'D')))
