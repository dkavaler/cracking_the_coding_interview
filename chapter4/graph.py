# Basic implementation of (directed) graph
class GraphNode:

    UNVISITED = 0
    VISITED = 1

    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited_state = GraphNode.UNVISITED

    def add_child(self, graph_node):
        self.children.append(graph_node)


class Graph:
    # Assumes node names are unique

    def __init__(self, node_names=[], directed=True):
        self._graph = []
        for node_name in node_names:
            self._graph.append(GraphNode(node_name))

    # Assumes all nodes have been initialized and are contained in self._graph
    def add_edge(self, start_name, end_name):
        start_node = self.find_node_by_name(start_name)
        end_node = self.find_node_by_name(end_name)
        start_node.add_child(end_node)

    # Returns a new node if the specified name is not found
    # in the graph
    def find_node_by_name(self, name):
        for node in self._graph:
            if node.name == name:
                return node

        return GraphNode(name)

    # The only invalid build order is one in which there is a cycle
    # somewhere in the graph.
    # Since there can be "islands", we have to test this for every node.
    # DFS is the easiest way to check this.
    def has_cycle(self):
        for i in range(len(self._graph)):
            start_node = self._graph[i]
            visited, stack = set(), [start_node]
            while stack:
                n = stack.pop()
                if n in visited and n == start_node:
                    return True
                elif n not in visited:
                    visited.add(n)
                    stack.extend(n.children)

        return False

    # Assumes no cycles
    def _dfs_visit(self, node, order):
        if node.visited_state == GraphNode.UNVISITED:
            node.visited_state = GraphNode.VISITED
            for child in node.children:
                self._dfs_visit(child, order)
            order.insert(0, node)
            
                
    def topological_order(self):
        if self.has_cycle():
            raise Exception('Cycle detected, no possible build order.')

        # Now that we know there's no cycle,
        # get a valid build order.
        # The trick is to put the visited order IN FRONT of the existing order.
        order = []
        for node in self._graph:
            if node.visited_state == GraphNode.UNVISITED:
                self._dfs_visit(node, order)

        return order


