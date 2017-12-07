from node import Node


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


# BFS is the easiest way I can think to do this
def list_of_depths(root):
    q = [(root, 0)]
    visited = {root: True}
    depth_list = []
    while len(q) > 0:
        n, level = q.pop(0)

        if len(depth_list) == level:
            depth_list.append([])
        depth_list[level].append(n)

        for child in n.children:
            if child and child not in visited:
                visited[child] = True
                q.append((child, level + 1))

    return depth_list



if __name__ == '__main__':
    # Construct a binary tree
    # Easier to use the method from 4.2
    inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = create_bst(inp)
    depth_list = list_of_depths(bst)
    for l in depth_list:
        print([el.data for el in l])
    