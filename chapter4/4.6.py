from node import create_bst


def successor(node):
    if node.get_child(1):
        return get_leftmost(node.get_child(1))

    n = node
    p = n.parent
    while p and p.get_child(0) != n:
        n = p
        p = p.parent

    return p


def get_leftmost(node):
    if not node:
        return None

    cur_node = node
    while cur_node.get_child(0):
        cur_node = cur_node.get_child(0)

    return cur_node


def set_parents(root):
    for child in root.children:
        if child:
            child.parent = root
            set_parents(child)


if __name__ == '__main__':
    bst = create_bst([1, 2, 3, 4, 5, 6, 7, 8, 9])
    set_parents(bst)
    
    assert successor(bst).data == 6
    assert successor(bst.get_child(0)).data == 3
    assert successor(bst.get_child(0).get_child(1)).data == 4
    assert successor(bst.get_child(0).get_child(1).get_child(1)).data == 5
    assert successor(bst.get_child(1)).data == 8
    assert successor(bst.get_child(1).get_child(1)).data == 9
    assert successor(bst.get_child(1).get_child(0)).data == 7