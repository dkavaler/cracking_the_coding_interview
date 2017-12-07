from node import create_bst, Node

# Creates an unbalanced binary tree
def create_unbalanced_binary_tree(inp):
    root = Node(data=inp[0])
    cur_node = root
    for el in inp:
        new_node = Node(data=el)
        cur_node.add_child(new_node, 0)
        cur_node = new_node

    return root


def is_bst(root, min_v, max_v):
	if root is None:
		return True

	if (min_v and root.data <= min_v) or (max_v and root.data > max_v):
		return False

	flag = True
	lc = root.get_child(0)
	rc = root.get_child(1)

	if lc:
		flag &= lc.data <= root.data
	if rc:
		flag &= rc.data > root.data

	if not flag:
		return False


	return is_bst(lc, min_v, root.data) and is_bst(rc, root.data, max_v)


if __name__ == '__main__':
	bst = create_bst([1, 2, 3, 4, 5, 6, 7, 8])
	print(is_bst(bst, None, None))

	u_bst = create_unbalanced_binary_tree([1, 2, 3, 4, 5, 6, 7, 8])
	print(is_bst(u_bst, None, None))

	u_bst = create_unbalanced_binary_tree([8, 7, 6, 5, 4, 3, 2, 1])
	print(is_bst(u_bst, None, None))