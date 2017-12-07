from node import Node

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
    # Recursive version
    root_node = create_bst(inp)
    root_node.inorder_print_binary()

