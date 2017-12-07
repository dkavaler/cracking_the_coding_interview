from node import create_bst, Node

# BFS to get depth of tree
def get_depth(root):
    if not root:
        return 0

    q = [(root, 0)]
    visited = {root: True}
    max_depth = 0

    while len(q) > 0:
        node, level = q.pop(0)

        if level > max_depth:
            max_depth = level

        for child in node.children:
            if child and child not in visited:
                visited[child] = True
                q.append((child, level + 1))

    return max_depth


def check_balanced(root):
    return abs(get_depth(root.get_child(0)) - get_depth(root.get_child(1))) <= 1


# Creates an unbalanced binary tree
def create_unbalanced_binary_tree(inp):
    root = Node(data=inp[0])
    cur_node = root
    for el in inp:
        new_node = Node(data=el)
        cur_node.add_child(new_node, 0)
        cur_node = new_node

    return root



if __name__ == '__main__':
    bst = create_bst([1, 2, 3, 4, 5, 6, 7])
    print(check_balanced(bst))

    u_bst = create_unbalanced_binary_tree([1, 2, 3, 4, 5, 6, 7])
    print(check_balanced(u_bst))

