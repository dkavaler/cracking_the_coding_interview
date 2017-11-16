class ListNode:

    def __init__(self, d=None):
        self.next = None
        self.data = d


# Singly linked to make things harder
class LinkedList:

    def __init__(self, d=None):
        self.head = ListNode(d)

    def append(self, d):
        n = self.head
        if not n.data:
            n.data = d
            return

        while n.next:
            n = n.next

        n.next = ListNode(d)

    # 2.1 with buffer
    def remove_duplicates_wbuffer(self):
        buf = {}
        n = self.head
        prev = None

        while n:
            if n.data in buf:
                prev.next = n.next
            else:
                buf[n.data] = True
                prev = n
            n = n.next

    # 2.1 no buffer
    # Uses an extra pointer when compared to the book's solution,
    # but is similar to the wbuffer solution so easier to read in my opinion
    def remove_duplicates_nobuffer(self):
        n = self.head

        while n:
            ahead = n.next
            prev = n
            while ahead:
                if n.data == ahead.data:
                    prev.next = ahead.next
                else:
                    prev = ahead

                ahead = ahead.next

            n = n.next


    # Trivially easy version
    def get_k_last(self, k):
        # Get length of list
        length = 0
        n = self.head
        while n:
            length += 1
            n = n.next

        if k >= length:
            return None

        n = self.head
        for i in range(length - 1 - k):
            n = n.next

        return n

    # Harder version, not allowed to explicitly calculate list length
    # Use 2 pointers - one counts for k, then move the trailing pointer
    # until forward pointer hits end of list.
    # Definition operates as: 
    #   0th last = last element, 1st last = second to last element
    def get_k_last_hard(self, k):
        k_n = self.head
        item_n = self.head

        i = 0
        while k_n and i < k:
            k_n = k_n.next
            i += 1

        if not k_n:
            return None

        while k_n.next:
            k_n = k_n.next
            item_n = item_n.next

        return item_n


    # Not allowed to use head, only del_node
    def delete_middle_node(self, del_node):
        next_n = del_node.next
        # Deleting from end of list, not allowed
        if not next_n:
            return -1

        del_node.data = next_n.data
        del_node.next = next_n.next

    # The description in the book is a little confusing, but I think this is a proper
    # implementation.
    def partition(self, value):
        n = self.head
        less_list = LinkedList(None)
        more_list = LinkedList(None)
        while n:
            if n.data < value:
                less_list.append(n.data)
            else:
                more_list.append(n.data)

            n = n.next


        # Concatenate less_list and more_list
        # and update self
        n_less = less_list.head
        while n_less.next:
            n_less = n_less.next

        n_less.next = more_list.head

        self.head = less_list.head




def iterate_aggregate(ll):
    n = ll.head
    agg = []
    while n:
        agg.append(n.data)
        n = n.next

    return agg


def check_2_1_1(ll):
    ll.remove_duplicates_wbuffer()
    assert iterate_aggregate(ll) == [1, 2, 3, 4, 5]


def check_2_1_2(ll):
    ll.remove_duplicates_nobuffer()
    assert iterate_aggregate(ll) == [1, 2, 3, 4, 5]


def check_2_2_1(ll):
    assert ll.get_k_last(0).data == 5
    assert ll.get_k_last(1).data == 4
    assert ll.get_k_last(2).data == 3
    assert ll.get_k_last(3).data == 2
    assert ll.get_k_last(4).data == 1
    assert ll.get_k_last(5) == None
    assert ll.get_k_last(6) == None


def check_2_2_2(ll):
    assert ll.get_k_last_hard(0).data == 5
    assert ll.get_k_last_hard(1).data == 4
    assert ll.get_k_last_hard(2).data == 3
    assert ll.get_k_last_hard(3).data == 2
    assert ll.get_k_last_hard(4).data == 1
    assert ll.get_k_last_hard(5) == None
    assert ll.get_k_last_hard(6) == None


def check_2_3(ll):
    node = ll.get_k_last(3)
    ll.delete_middle_node(node)
    assert iterate_aggregate(ll) == [1, 3, 4, 5]


def check_2_4(ll):
    ll.partition(3)
    assert iterate_aggregate(ll) == [1, 2, 5, 3, 6, 4]


def create_linkedlist():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(4)
    ll.append(5)
    ll.append(5)

    return ll

def create_unordered_linkedlist():
    ll = LinkedList(1)
    ll.append(5)
    ll.append(3)
    ll.append(6)
    ll.append(2)
    ll.append(4)

    return ll


if __name__ == '__main__':
    ll = create_linkedlist()
    # 2.1 checks
    check_2_1_1(ll)
    ll = create_linkedlist()
    check_2_1_2(ll)

    # 2.2 check
    check_2_2_1(ll)
    check_2_2_2(ll)

    # 2.3 check
    check_2_3(ll)

    # 2.4 check
    ll = create_unordered_linkedlist()
    check_2_4(ll)





