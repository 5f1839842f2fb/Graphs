"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id, edges=[]):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set(edges)

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = [starting_vertex]
        visited = {starting_vertex}
        while len(queue) > 0:
            vertex = queue.pop(0)
            visited.add(vertex)
            for edge in self.vertices[vertex]:
                if edge not in visited and edge not in queue:
                    queue += [edge]
            print(vertex) 
                

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = [starting_vertex]
        visited = {starting_vertex}
        while len(stack) > 0:
            vertex = stack.pop(-1)
            visited.add(vertex)
            for edge in self.vertices[vertex]:
                if edge not in visited and edge not in stack:
                    stack += [edge]
            print(vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = {starting_vertex} # this is only because empty {} creates a dictionary, not a set, despite {whatever} creating a set
        def recurs(starting_vertex):
            visited.add(starting_vertex)
            print(starting_vertex)
            for vertex in self.vertices[starting_vertex]:
                if vertex not in visited:
                    recurs(vertex)
        recurs(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        paths = [[starting_vertex]]
        while len(paths) > 0:
            path = paths.pop(0)
            node = path[-1]
            if node == destination_vertex:
                return path
            if node not in visited:
                visited.add(node)
                for edge in self.vertices[node]:
                    paths += [path + [edge]]


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        paths = [[starting_vertex]]
        while len(paths) > 0:
            path = paths.pop(-1)
            node = path[-1]
            if node == destination_vertex:
                return path
            if node not in visited:
                visited.add(node)
                for edge in self.vertices[node]:
                    paths += [path + [edge]]

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        shortest = []
        def recurs(path, destination_vertex):
            if len(shortest) > 0:
                return
            starting_vertex = path[-1]
            if starting_vertex == destination_vertex:
                shortest.extend(path)
            if starting_vertex not in visited:
                visited.add(starting_vertex)
                for edge in self.vertices[starting_vertex].difference(visited):
                    recurs(path+[edge], destination_vertex)

        recurs([starting_vertex], destination_vertex)
        return shortest

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
