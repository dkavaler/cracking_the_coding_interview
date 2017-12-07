from node import Node


class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        cur_node = self.root
        added = False
        while not added:
            # Check left
            if node.data < cur_node.data:
                if cur_node.get_child(0):
                    cur_node = cur_node.get_child(0)
                else:
                    cur_node.add_child(node, pos=0)
                    added = True
            else:
                if cur_node.get_child(1):
                    cur_node = cur_node.get_child(1)
                else:
                    cur_node.add_child(node, pos=1)
                    added = True

    def inorder_print(self):
        self.root.inorder_print_binary()


# Recursive method (much faster)
def create_bst(arr):
    return _create_bst(arr, 0, len(arr) - 1)

def _create_bst(arr, start, end):
    if end < start:
        return None

    mid_point = (start + end) // 2
    mid_node = Node(data=arr[mid_point])
    left_node = _create_bst(arr, start, mid_point - 1)
    right_node = _create_bst(arr, mid_point + 1, end)
    mid_node.add_child(left_node, pos=0)
    mid_node.add_child(right_node, pos=1)

    return mid_node



if __name__ == '__main__':
    inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Minimal height = root element is inp[length(inp) // 2]
    root_el = inp[len(inp) // 2]
    bst = BinarySearchTree(Node(data=root_el))
    for el in inp:
        if el != root_el:
            bst.add_node(Node(data=el))
    bst.inorder_print()

    # Recursive version
    root_node = create_bst(inp)
    root_node.inorder_print_binary()

