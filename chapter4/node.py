class Node:

    def __init__(self, name=None, data=None):
        self.name = name
        self.data = data
        self.children = []


    def is_full(self, full_len):
        occupancy = [1 if child else 0 for child in self.children]
        return sum(occupancy) == len(self.children) or len(self.children) == full_len


    def add_child(self, node, pos=None):
        if not pos:
            self.children.append(node)
        else:
            if len(self.children) <= pos:
                for i in range(len(self.children), pos + 1):
                    self.children.append(None)
            self.children[pos] = node


    def get_child(self, pos):
        if len(self.children) <= pos:
            return None

        return self.children[pos]


    def inorder_print_binary(self):

        lc = self.get_child(0)
        if lc:
            lc.inorder_print_binary()
        print(self.data)
        rc = self.get_child(1)
        if rc:
            rc.inorder_print_binary()

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