class Graph:

    def __init__(self, adj_list={}):
        self.adj_list = adj_list


class DirectedGraph(Graph):

    def __init__(self, adj_list={}):
        super().__init__(adj_list)


    # Assuming you want to see if you can get to n2 from n1
    def path_exists(self, n1, n2):
        # Do search from n1 to n2, then n2 to n1
        return n2 in self.bfs(n1)

    # Returns node list that is reachable from source
    def bfs(self, source):
        q, reachable = [source], []
        visited = {source: True}

        while len(q) > 0:
            node = q.pop(0)
            reachable.append(node)
            if node not in adj_list:
                return 1

            for adj in adj_list[node]:
                if adj not in visited:
                    visited[adj] = True
                    q.append(adj)

        return reachable






if __name__ == '__main__':
    adj_list = {1: [2],
                2: [1, 3],
                3: [1, 2, 5],
                4: [],
                5: [4],
                6: []}
    g = DirectedGraph(adj_list)
    print(g.path_exists(1, 6))
    print(g.path_exists(1, 4))


    
