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


    def append_node(self, new_n):
        n = self.head
        
        while n.next:
            n = n.next

        n.next = new_n

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


    # Assuming it's 2, 3 digit numbers
    def sum_list_reverse(self):
        first_num_n = self.head
        second_num_n = self.get_k_last(2)
        ret_list = LinkedList(None)

        carry = 0
        for i in range(3):
            value = (first_num_n.data + second_num_n.data + carry) % 10
            carry = (first_num_n.data + second_num_n.data) // 10
            ret_list.append(value)

            first_num_n = first_num_n.next
            second_num_n = second_num_n.next

        if carry > 0:
            ret_list.append(carry)

        return ret_list


    # Multiple methods to do this - can reverse the elements and then pass
    # to sum_list_reverse, or do it some other way.
    # Reversing is the easiest obvious solution, but quite inefficient.
    # Can also run through, make a temp list copy, etc, should be O(N)
    def sum_list_forward(self):
        reverse_list = self.get_reverse_list()
        sum_list = reverse_list.sum_list_reverse()

        return sum_list.get_reverse_list()



    def get_reverse_list(self):
        reverse_list = LinkedList(None)
        n = self.head
        i = 0
        while n:
            reverse_list.append(self.get_k_last(i).data)
            n = n.next
            i += 1

        return reverse_list

    # Reverse it, check equality
    def is_palindrome(self):
        reverse_list = self.get_reverse_list()
        n1 = self.head
        n2 = reverse_list.head

        while n1 and n2:
            if n1.data != n2.data:
                return False
            
            n1 = n1.next
            n2 = n2.next

        return True


def get_cut_list(l, len):
    n = l.head
    for i in range(len):
        n = n.next

    return n


# If two lists end in same node, they're intersecting.
# To get the intersection, get the lengths of both lists,
# "cut" the longer one to be the size of the shorter, then
# go node by node
def get_intersection(ll1, ll2):
    n1, n2 = ll1.head, ll2.head
    ll1_len, ll2_len = 0, 0

    while n1:
        n1 = n1.next
        ll1_len += 1

    while n2:
        n2 = n2.next
        ll2_len += 1

    if n1 == n2:
        n1, n2 = ll1.head, ll2.head
        if ll1_len < ll2_len:
            n2 = get_cut_list(ll2, ll2_len - ll1_len)
        elif ll1_len > ll2_len:
            n1 = get_cut_list(ll1, ll1_len - ll2_len)

        while n1 and n2:
            if n1 == n2:
                return n1

            n1, n2 = n1.next, n2.next

    else:
        return None




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


def check_2_5_1(ll):
    assert iterate_aggregate(ll.sum_list_reverse()) == [5, 8, 7]


def check_2_5_2(ll):
    assert iterate_aggregate(ll.sum_list_forward()) == [1, 5, 7, 7]


def check_2_6(ll):
    assert ll.is_palindrome()
    ll.delete_middle_node(ll.get_k_last(2))
    assert not ll.is_palindrome()


def check_2_7(ll1, ll2):
    assert get_intersection(ll1, ll2)
    assert not get_intersection(create_linkedlist(), create_linkedlist())
    ll1.delete_middle_node(ll1.get_k_last(1))
    assert get_intersection(ll1, ll2)


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


def create_intersecting_linkedlists():
    ll1 = LinkedList(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    ll1.append(5)
    ll2 = LinkedList('a')
    ll2.append('b')
    ll2.append('c')
    ll2.append_node(ll1.get_k_last(1))

    return ll1, ll2


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

    # 2.5 check
    ll = LinkedList(9)
    ll.append(5)
    ll.append(3)
    ll.append(6)
    ll.append(2)
    ll.append(4)
    check_2_5_1(ll)
    check_2_5_2(ll)

    ll = LinkedList('a')
    ll.append('b')
    ll.append('c')
    ll.append('d')
    ll.append('c')
    ll.append('b')
    ll.append('a')

    check_2_6(ll)


    ll1, ll2 = create_intersecting_linkedlists()
    check_2_7(ll1, ll2)




