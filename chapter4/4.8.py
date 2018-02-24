class TreeNode:

    def __init__(self, name, left=None, right=None, parent=None):
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent

class BinaryTree:

    def __init__(self, node_list):
        self.root = TreeNode(node_list[0][0])
        self.root.left = self.find_node_by_name(node_list[0][1])
        if self.root.left:
            self.root.left.parent = self.root
        self.root.right = self.find_node_by_name(node_list[0][2])
        if self.root.right:
            self.root.right.parent = self.root
        for node_tup in node_list[1:]:
            node = self.find_node_by_name(node_tup[0])
            left = self.find_node_by_name(node_tup[1])
            if left:
                left.parent = node
            right = self.find_node_by_name(node_tup[2])
            if right:
                right.parent = node
            node.left = left
            node.right = right


    def find_node_by_name(self, name):
        if name == None:
            return None

        q, visited = [self.root], set()
        while q:
            n = q.pop(0)
            if n.name == name:
                return n
            if n not in visited:
                visited.add(n)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return TreeNode(name)

    def has_node(self, name):
        if name == None:
            return False

        q, visited = [self.root], []
        while q:
            n = q.pop(0)
            if n.name == name:
                return True
            if n not in visited:
                visited.append(n)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return False

    def bfs(self, node):
        q, visited = [node], []
        while q:
            n = q.pop(0)
            if n not in visited:
                visited.append(n)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return visited

    def first_common_ancestor_parents(self, name1, name2):
        if not self.has_node(name1) or not self.has_node(name2):
            return None

        node1 = self.find_node_by_name(name1)
        node2 = self.find_node_by_name(name2)

        # Same node, return it
        if node1 == node2:
            return node1

        # If node 2 is contained in the subtree rooted at 
        # node 1, node 1 is the first common ancestor
        if node2 in self.bfs(node1):
            return node1

        # And vice versa
        if node1 in self.bfs(node2):
            return node2

        # Move up the tree using one node, until the subtree
        # contains both nodes.
        # This implementation is O(n^2)
        fca = node1.parent
        while fca:
            if node2 in self.bfs(fca) and node1 in self.bfs(fca):
                return fca
            fca = fca.parent

    def first_common_ancestor_noparents(self, name1, name2):
        if not self.has_node(name1) or not self.has_node(name2):
            return None

        node1 = self.find_node_by_name(name1)
        node2 = self.find_node_by_name(name2)

        if node1 == node2:
            return node1

        if node2 in self.bfs(node1):
            return node1

        if node1 in self.bfs(node2):
            return node2

        # Walk from the root, going to the lowest level where
        # an element's subtree contains both nodes.
        # Since BFS is a level-order traversal, we can do a bfs,
        # walk through the reversed results, then exit out once we find
        # subtree node that contains both node1 and node2
        # This is O(n^2)
        level_order = self.bfs(self.root)
        for node in reversed(level_order):
            if node1 in self.bfs(node) and node2 in self.bfs(node):
                return node
        
        


        


if __name__ == '__main__':
    node_list = [('F', 'B', 'C'), ('B', 'D', 'E'), ('E', None, 'A')]
    bt = BinaryTree(node_list)

    assert bt.first_common_ancestor_parents('X', 'Z') is None
    assert bt.first_common_ancestor_parents('E', 'A').name == 'E'
    assert bt.first_common_ancestor_parents('D', 'E').name == 'B'
    assert bt.first_common_ancestor_parents('A', 'C').name == 'F'
    assert bt.first_common_ancestor_parents('B', 'A').name == 'B'
    assert bt.first_common_ancestor_parents('B', 'B').name == 'B'

    # Without using parent pointers
    assert bt.first_common_ancestor_noparents('E', 'A').name == 'E'
    assert bt.first_common_ancestor_noparents('D', 'E').name == 'B'
    assert bt.first_common_ancestor_noparents('A', 'C').name == 'F'
    assert bt.first_common_ancestor_noparents('B', 'A').name == 'B'
    assert bt.first_common_ancestor_noparents('B', 'B').name == 'B'
